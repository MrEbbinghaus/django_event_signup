from django.conf.urls import url

from . import views

urlpatterns = [
    # your routing urls here
    url(r'^(?P<event_id>[0-9]+)$', views.event_view, name='event_view'),
    url(r'^staff/(?P<event_id>[0-9]+)$', views.staff_view, name='staff_view'),
]
