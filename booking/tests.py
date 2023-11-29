from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Appointment
from profiles.models import UserProfile
from django.contrib.auth.models import User
from products.models import Item, Category
from checkout.models import Order
from datetime import datetime, timedelta, date, time
from .views import getDaysOfWeekForDay, sortSessionsByDay
import pytz

# Create your tests here.


class BookingTests(TestCase):

    # Test the creation of a appointment
    def test_create_appointment(self):

        # Create a user for the appointment
        user = User.objects.create(email="normal@user.de", username="test", password="dodo")   # noqa
        user.save()

        # Get userprofile
        userprofile = UserProfile.objects.get(user=user)

        # Create new product category
        category = Category.objects.create(name="testcategory", friendly_name="testcategory")   # noqa
        category.save()

        # Create new item
        item = Item.objects.create(
            category=category,
            name="name",
            sku="sku",
            price=10,
            discount_price=1,
            description="description",
            )   # noqa
        item.save()

        t = datetime.now()

        # Create order
        order = Order.objects.create(
                    order_number='order_number',
                    user_profile=userprofile,
                    full_name='full_name',
                    email='email@email.com',
                    phone_number='0792873928',
                    country='DE',
                    postcode='',
                    town_or_city='town_or_city',
                    street_address1='street_address1',
                    street_address2='street_address2',
                    county='county',
                    date=t,
                    delivery_cost=1,
                    order_total=12,
                    grand_total=13,
                    original_bag='original_bag',
                    stripe_pid='stripe_pid',
                    )   # noqa
        order.save()

        # Create appointment
        appointment = Appointment.objects.create(user=userprofile,
                                             item=item,
                                             order=order,
                                             time=t,
                                             duration=timedelta(minutes=60))   # noqa

        appointment.save()
        all_user_appointments = Appointment.objects.filter(user=userprofile)

        # Test appointment is setup correctly
        self.assertEqual(len(all_user_appointments), 1)
        for s in all_user_appointments:
            print(s)
            self.assertEqual(s.user, userprofile)
            self.assertEqual(s.item, item)
            self.assertEqual(s.order, order)
            self.assertEqual(s.time, t)
            self.assertEqual(s.duration, timedelta(minutes=60))

    def test_subfunctions(self):

        # Create new user
        user = User.objects.create(email="normal@user.de", username="test", password="dodo")   # noqa
        user.save()

        # Create user profile
        userprofile = UserProfile.objects.get(user=user)

        # Create category
        category = Category.objects.create(name="testcategory", friendly_name="testcategory")   # noqa
        category.save()

        # Create item
        item = Item.objects.create(
            category=category,
            name="name",
            sku="sku",
            price=10,
            discount_price=1,
            description="description",
            )   # noqa
        item.save()

        t = datetime(2023, 8, 15, 8, 0, 0)   # noqa

        # Create order
        order = Order.objects.create(
                    order_number='order_number',
                    user_profile=userprofile,
                    full_name='full_name',
                    email='email@email.com',
                    phone_number='0792873928',
                    country='DE',
                    postcode='',
                    town_or_city='town_or_city',
                    street_address1='street_address1',
                    street_address2='street_address2',
                    county='county',
                    date=t,
                    delivery_cost=1,
                    order_total=12,
                    grand_total=13,
                    original_bag='original_bag',
                    stripe_pid='stripe_pid',
                    )   # noqa
        order.save()

        # Create appointments at various times
        appointment1 = Appointment.objects.create(user=userprofile,
                                             item=item,
                                             order=order,
                                             time=t,
                                             duration=timedelta(minutes=60))   # noqa
        appointment1.save()

        appointment2 = Appointment.objects.create(user=userprofile,
                                             item=item,
                                             order=order,
                                             time=t+timedelta(hours=1),
                                             duration=timedelta(minutes=60))   # noqa
        appointment2.save()

        appointment3 = Appointment.objects.create(user=userprofile,
                                             item=item,
                                             order=order,
                                             time=t+timedelta(hours=2),
                                             duration=timedelta(minutes=60))   # noqa
        appointment3.save()

        appointment4 = Appointment.objects.create(user=userprofile,
                                             item=item,
                                             order=order,
                                             time=t+timedelta(hours=3),
                                             duration=timedelta(minutes=60))   # noqa
        appointment4.save()

        days_of_the_week, weekday = getDaysOfWeekForDay(t)
        self.assertEqual(weekday, 1)
        self.assertEqual(days_of_the_week[0], '08/14/2023')  # Monday
        self.assertEqual(days_of_the_week[6], '08/20/2023')  # Sunday

        # Check in database for existing appointments during that week
        start_dt = t.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=(0-weekday))   # noqa
        end_dt = start_dt + timedelta(days=7)
        all_appointments = Appointment.objects.filter(time__gte=start_dt, time__lt=end_dt)   # noqa

        appointments_of_the_week = sortSessionsByDay(all_appointments, days_of_the_week, user)   # noqa

        for d in days_of_the_week:
            if d == weekday:
                self.assertEqual(len(appointments_of_the_week[d]), 4)
            else:
                self.assertEqual(len(appointments_of_the_week[d]), 0)
