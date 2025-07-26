from django.contrib import admin
from .models import UserProfile, Medicine, Appointment, VitalLog

admin.site.register(UserProfile)
admin.site.register(Medicine)
admin.site.register(Appointment)
admin.site.register(VitalLog)
# Register your models here.
