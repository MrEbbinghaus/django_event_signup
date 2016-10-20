from django.contrib.auth.models import User
from django.db import models


class Event(models.Model):
    date = models.DateField(blank=False)
    name = models.CharField(blank=False, max_length=64)
    location = models.TextField(blank=True)

    class Meta:
        get_latest_by = 'date'

    def __str__(self):
        display = "{0} am {1}"
        return display.format(self.user, self.event)


class Participant(models.Model):
    user = models.ForeignKey(User)
    event = models.ForeignKey(Event)

    class Meta:
        unique_together = ('user', 'event')

    def __str__(self):
        display = "Teilnahme von {0} an {1}"
        return display.format(self.user, self.event)
