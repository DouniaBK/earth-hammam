from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from datetime import datetime, timezone, timedelta
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from .forms import AppointmentInputFormFrontEnd
from django.contrib import messages
from profiles.models import UserProfile
from products.models import Item
from .models import Appointment
import json


def getDaysOfWeekForDay(t_current):
    """Returns the days of the week for a specific day"""
    weekday = t_current.weekday()

    days_of_the_week = {}
    for i in range(0 - weekday, 7 - weekday):
        t_day = t_current + timedelta(days=i)
        days_of_the_week[t_day.weekday()] = t_day.strftime("%m/%d/%Y")

    return days_of_the_week, weekday


def sortSessionsByDay(all_sessions, days_of_the_week, user):
    """Sort all_sessions by the day they occur"""
    sessions_of_the_week = {}
    # Iterate over all weekdays
    for d in days_of_the_week:
        # Filter the sessions that occur on the specific day
        date_of_that_day = days_of_the_week[d]
        date_time_object_lower = datetime.strptime(
            date_of_that_day, "%m/%d/%Y")
        date_time_object_upper = date_time_object_lower + timedelta(days=1)
        days_sessions = all_sessions.filter(
            time__gte=date_time_object_lower, time__lte=date_time_object_upper
        )

        sessions_of_the_week[d] = []
        for s in days_sessions:
            sessions_time_hours = s.time.strftime("%H")
            isme = s.user == user
            if isme:
                sessions_time_hours = sessions_time_hours + "me"
            sessions_of_the_week[d].append(sessions_time_hours)
    return sessions_of_the_week


def getOffsetFromRequest(request):
    """Extract the week offset from the request, return 0 if not defined"""
    offset_param = int(request.GET.get("offset", "0"))
    # In case a negative value is given, set back to zero
    # (protection against manual URL manipulation)
    if offset_param < 0:
        offset_param = 0
    return offset_param


def booking(request):
    """This view acts as middleware for the calendar, thus assembling all
    necessary information for viewing the calendar
    and handling session booking and cancelation"""
    try:
        # Special variable to indicate whether
        # the booking is done in the context of the new registration
        register_to_book = request.GET.get("rtb", "false") == "true"
        # Special variable to indicate whether
        # the register and booking workflow was successful
        success = False
        if register_to_book:
            success = request.GET.get("success", "false") == "true"

        h_min = 8
        h_max = 21

        offset_param = getOffsetFromRequest(request)
        offset_weeks = timedelta(weeks=offset_param)

        t_current = datetime.now() + offset_weeks

        # The all days of the current week and current weekday as int
        days_of_the_week, weekday = getDaysOfWeekForDay(t_current)

        # Check in database for existing sessions during that week
        start_dt = t_current.replace(
            hour=0, minute=0, second=0, microsecond=0
        ) + timedelta(days=(0 - weekday))
        end_dt = start_dt + timedelta(days=7)
        all_sessions = Appointment.objects.filter(
            time__gte=start_dt, time__lt=end_dt)

        sessions_of_the_week = sortSessionsByDay(
            all_sessions, days_of_the_week, request.user
        )

        # Fill in all sessions in the past
        #  (grey out past days sessions in scheduler)
        week_now = int(datetime.now().strftime("%V"))
        week_current = int(t_current.strftime("%V"))
        if week_current == week_now:
            for d in days_of_the_week:
                if d <= weekday:
                    for i in range(h_min, h_max):
                        if (
                            not str(i) in sessions_of_the_week[d]
                            and not (str(i) + "me") in sessions_of_the_week[d]
                        ):
                            sessions_of_the_week[d].append(str(i))

        user = None
        is_authenticated = False
        try:
            user = UserProfile.objects.get(user=request.user)
            is_authenticated = True
        except Exception as e:
            pass

        # Get all appointments of the user
        all_user_sessions_templ = []
        all_user_sessions = []
        try:
            all_user_sessions = Appointment.objects.filter(user=user)
        except Exception as e:
            pass

        for us in all_user_sessions:
            info = {}
            info["id"] = us.id
            info["service"] = us.item
            info["time"] = us.time.strftime("%m/%d/%Y at %H:%M")

            all_user_sessions_templ.append(info)

        # Assemble which hours need to be shown in the calendar
        hours_vec = []
        for i in range(h_min, h_max):
            hours_vec.append(str(i))

        treatments = Item.objects.filter(category=1)
        all_treatments = []
        treatment_ids_vec = []
        for treatment in treatments:
            trtm = {}
            trtm["id"] = treatment.id
            trtm["name"] = treatment.name
            trtm["description"] = treatment.description
            trtm["image"] = treatment.image.url

            treatment_ids_vec.append(str(treatment.id))
            all_treatments.append(trtm)

        # if this is a POST request, handle saving the session
        if (request.method == "POST") and (is_authenticated == True):
            form = AppointmentInputFormFrontEnd(request.POST)

            service = form["service"]
            id = int(service.data)
            item = Item.objects.get(id=id)

            # check whether the form is valid:
            if form.is_valid():
                session_object = form.save(commit=False)
                session_object.user = user
                session_object.item = item
                session_object.save()
                # process the data in form.cleaned_data as required
                service = form.cleaned_data["service"]
                time = form.cleaned_data["time"]
                # redirect to a new URL:
                if register_to_book:
                    return HttpResponseRedirect(
                        "/booking?rtb=true&success=true")
                else:
                    return HttpResponseRedirect(
                        "/booking?offset=" + str(offset_param))
            else:
                print("Error", form.errors)

        form = AppointmentInputFormFrontEnd()

        return render(
            request,
            "booking/booking.html",
            {
                "form": form,
                "weekdays": days_of_the_week,
                "currentWeekOffset": offset_param,
                "weeksSessions": sessions_of_the_week,
                "allUserSessions": all_user_sessions_templ,
                "scheduleHours": hours_vec,
                "isThisWeek": week_current == week_now,
                "register_to_book": register_to_book,
                "register_book_success": success,
                "scheduleHours_json": json.dumps(hours_vec),
                "treatment_ids_json": json.dumps(treatment_ids_vec),
                "treatments": all_treatments,
                "is_authenticated": is_authenticated,
            },
        )
    except Exception as e:
        print(str(e), e.args)
        return HttpResponseRedirect("")


@login_required
def cancel_session(request):
    """This cancels a booking/session"""
    try:
        # Get the offset parameter from the request
        offset_param = getOffsetFromRequest(request)

        # Get session ID
        id = int(request.GET.get("id", "-1"))

        # Get session
        booked_session = get_object_or_404(Appointment, id=id)

        # Get user
        user = UserProfile.objects.get(user=request.user)

        # Only the owner can delete the session - updated
        is_same_user = user == booked_session.user

        if (request.method == "GET") and (is_same_user == True):
            booked_session.delete()
            return HttpResponseRedirect("/booking?offset=" + str(offset_param))
        raise PermissionDenied

    except Exception as e:
        raise PermissionDenied
