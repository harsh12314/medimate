from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    emergency_contact = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user.username


class Medicine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100)
    frequency = models.CharField(max_length=100)  
    start_date = models.DateField(null=True, blank=True)  
    end_date = models.DateField(null=True, blank=True)    
    next_dose_time = models.DateTimeField(null=True, blank=True)  
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.user.username}"

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor_name = models.CharField(max_length=100)
    date = models.DateTimeField()
    purpose = models.CharField(max_length=200, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.doctor_name} on {self.date}"



class VitalLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    blood_pressure = models.CharField(max_length=20, blank=True)
    sugar_level = models.CharField(max_length=20, blank=True)
    weight = models.FloatField(null=True, blank=True)
    pulse = models.IntegerField(null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Vitals for {self.user.username} on {self.date}"

class Vitals(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    blood_pressure = models.CharField(max_length=20, blank=True)
    sugar_level = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"Vitals on {self.date} – {self.user.username}"

