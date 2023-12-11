from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, OrderLineItem
from products.models import Item
from profiles.models import UserProfile

import json
import time
import stripe


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """ Send the user a confirmation email """

        # Assemble content
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        content = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        body = render_to_string(
            'checkout/email_template.html',
            {'content': content})

        # Send email
        from_email = settings.DEFAULT_FROM_EMAIL
        to = cust_email
        text_content = content
        html_content = body
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    def _send_treatment_card_email(self, order, treatment_name):
        """ Send the user a treatment gift card email """
        # Assemble content
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/treatment_email_subject.txt',
            {'order': order})
        content = render_to_string(
            'checkout/confirmation_emails/treatment_email_body.txt',
            {
                'order': order,
                'contact_email': settings.DEFAULT_FROM_EMAIL,
                'treatment_type': treatment_name
            })

        body = render_to_string(
            'checkout/email_template.html',
            {'content': content})

        # Send email
        from_email = settings.DEFAULT_FROM_EMAIL
        to = cust_email
        text_content = content
        html_content = body
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    def _process_treatment_emails(self, order):
        """ Send gift card emails if applicable """
        l_items = OrderLineItem.objects.filter(order=order)
        for l_item in l_items:
            if l_item.item.category.name == 'Treatments':
                if l_item.item.name == 'Signature':
                    self._send_treatment_card_email(order, 'Signature')

                if l_item.item.name == 'Essential':
                    self._send_treatment_card_email(order, 'Essential')

                if l_item.item.name == 'Vital':
                    self._send_treatment_card_email(order, 'Vital')

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )

        billing_details = stripe_charge.billing_details  # updated
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2)  # updated
        print('handle_payment_intent_succeeded billing_details')
        print(billing_details)
        print('handle_payment_intent_succeeded shipping_details')
        print(shipping_details)
        print('handle_payment_intent_succeeded grand_total')
        print(grand_total)
        print('handle_payment_intent_succeeded pid')
        print(pid)

        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Update profile information if save_info was checked
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_phone_number = shipping_details.phone
                profile.default_country = shipping_details.address.country
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_town_or_city = shipping_details.address.city
                profile.default_street_address1 = shipping_details.address.line1   # noqa
                profile.default_street_address2 = shipping_details.address.line2     # noqa
                profile.default_county = shipping_details.address.state
                profile.save()
        
        # Retrieve order
        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        print('order_exists')
        print(order_exists)
        print('handle_payment_intent_succeeded order')
        try:
            print(order)
        except:
            print('NO')

        if order_exists:
            self._send_confirmation_email(order)
            self._process_treatment_emails(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: order already in database',   # noqa
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(bag).items():
                    item = Item.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            item=item,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():   # noqa
                            order_line_item = OrderLineItem(
                                order=order,
                                item=item,
                                quantity=quantity,
                                item_size=size,
                            )
                            order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        self._send_confirmation_email(order)
        self._process_treatment_emails(order)

        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',    # noqa
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
