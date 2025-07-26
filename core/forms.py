from django import forms
from .models import Appointment
from .models import Medicine
from .models import Vitals

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomSignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    date_of_birth = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    emergency_contact = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'date_of_birth', 'emergency_contact']


class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['name', 'dosage', 'frequency', 'start_date', 'end_date', 'next_dose_time', 'notes']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'next_dose_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor_name', 'date', 'purpose', 'notes']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class VitalsForm(forms.ModelForm):
    class Meta:
        model = Vitals
        fields = ['date', 'blood_pressure', 'sugar_level', 'weight']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
