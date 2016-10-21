from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_list_or_404, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.admin.views.decorators import staff_member_required

from django.contrib.auth.models import User
from .models import Event, Participant


@login_required()
def event_view(request, event_id):
    try:
        event = get_object_or_404(Event, id=event_id)

        context = {
            "event": event
        }

        return render(request, "django_event_signup/main_view.html", context)
    except Http404:
        return HttpResponse(code=404)


@staff_member_required()
def staff_view(request, event_id):
    try:
        entries = [user.email for user in get_list_or_404(User, participant__event_id=event_id)]

        context = {
            'entries': entries
        }

        return render(request, 'django_event_signup/staff_view.html', context)
    except Http404:
        return HttpResponse(code=404)
