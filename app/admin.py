from django.contrib import admin
from app.models import Gym,Trainer,Client,Slot,Booking

# Register your models here.
admin.site.register(Gym)
admin.site.register(Trainer)
admin.site.register(Client)
admin.site.register(Slot)
admin.site.register(Booking)