from django import forms
from .models import Appointment
from .models import Medicine
from .models import Vitals
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class CustomSignupForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(required=True)
    date_of_birth = forms.DateField(required=False)
    emergency_contact = forms.CharField(max_length=20, required=False)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already taken. Please choose a different one.")
        return username



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
