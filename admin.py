from django.contrib import admin
from .models import *

# here you define the models you want to see in the admin menu
admin.site.register(Event)
admin.site.register(Participant)