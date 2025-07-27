from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import UserProfile, Medicine
from .forms import MedicineForm
from .models import Appointment
from .forms import AppointmentForm
from .models import Vitals
from .forms import VitalsForm
from .forms import CustomSignupForm

import json
from django.core.serializers.json import DjangoJSONEncoder
# Homepage
def home(request):
    return render(request, 'home.html')

# Signup view
from .forms import CustomSignupForm
def signup_view(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            dob = form.cleaned_data['date_of_birth']
            emergency_contact = form.cleaned_data['emergency_contact']

            user = User.objects.create_user(username=username, email=email, password=password)

            UserProfile.objects.create(
                user=user,
                date_of_birth=dob,
                emergency_contact=emergency_contact
            )

            login(request, user)
            return redirect('profile')
    else:
        form = CustomSignupForm()
    return render(request, 'signup.html', {'form': form})


# Profile view
@login_required
def profile_view(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    medicines = Medicine.objects.filter(user=request.user)
    appointments = Appointment.objects.filter(user=request.user).order_by('date')
    vitals = Vitals.objects.filter(user=request.user).order_by('-date')[:5]  # latest 5

    return render(request, 'profile.html', {
        'profile': profile,
        'medicines': medicines,
        'appointments': appointments,
        'vitals': vitals
    })


# Medicine views
@login_required
def medicine_list(request):
    medicines = Medicine.objects.filter(user=request.user)
    return render(request, 'medicine_list.html', {'medicines': medicines})

@login_required
def add_medicine(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            medicine = form.save(commit=False)
            medicine.user = request.user
            medicine.save()
            return redirect('medicine_list')
    else:
        form = MedicineForm()
    return render(request, 'medicine_form.html', {'form': form})

@login_required
def edit_medicine(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk, user=request.user)
    if request.method == 'POST':
        form = MedicineForm(request.POST, instance=medicine)
        if form.is_valid():
            form.save()
            return redirect('medicine_list')
    else:
        form = MedicineForm(instance=medicine)
    return render(request, 'medicine_form.html', {'form': form})

@login_required
def delete_medicine(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk, user=request.user)
    if request.method == 'POST':
        medicine.delete()
        return redirect('medicine_list')
    return render(request, 'delete_medicine.html', {'medicine': medicine})


@login_required
def appointment_list(request):
    appointments = Appointment.objects.filter(user=request.user).order_by('date')
    return render(request, 'appointment_list.html', {'appointments': appointments})

@login_required
def add_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'appointment_form.html', {'form': form})

@login_required
def edit_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk, user=request.user)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'appointment_form.html', {'form': form})

@login_required
def delete_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk, user=request.user)
    if request.method == 'POST':
        appointment.delete()
        return redirect('appointment_list')
    return render(request, 'delete_appointment.html', {'appointment': appointment})


@login_required
def vitals_list(request):
    vitals = Vitals.objects.filter(user=request.user).order_by('date')
    return render(request, 'vitals_list.html', {'vitals': vitals})

@login_required
def add_vitals(request):
    if request.method == 'POST':
        form = VitalsForm(request.POST)
        if form.is_valid():
            vitals = form.save(commit=False)
            vitals.user = request.user
            vitals.save()
            return redirect('vitals_list')
    else:
        form = VitalsForm()
    return render(request, 'vitals_form.html', {'form': form})


@login_required
def vitals_graph(request):
    vitals = Vitals.objects.filter(user=request.user).order_by('date')

    dates = [v.date.strftime('%Y-%m-%d') for v in vitals]
    bp_values = [v.blood_pressure for v in vitals]
    sugar_levels = [v.sugar_level for v in vitals]
    weights = [v.weight for v in vitals]

    return render(request, 'vitals_graph.html', {
        'dates': json.dumps(dates, cls=DjangoJSONEncoder),
        'bp_values': json.dumps(bp_values, cls=DjangoJSONEncoder),
        'sugar_values': json.dumps(sugar_levels, cls=DjangoJSONEncoder),
        'weight_values': json.dumps(weights, cls=DjangoJSONEncoder),
    })
