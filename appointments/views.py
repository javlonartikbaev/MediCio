from django.shortcuts import render, redirect

from .forms import AppointmentForm
from .models import *
from datetime import datetime
from random import randint

# Create your views here.


def all_doctors_services(request):
    doctors = Doctors.objects.all()
    services = Service.objects.all()

    curent_year = datetime.today().year
    data = {'doctors': doctors
        , 'services': services,
            'curent_year': curent_year,
            }
    return render(request, 'appointments/index.html', data)


def appointment_form(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            selected_services = form.cleaned_data['service_id']
            appointment.medical_insurance = randint(100000000, 1000000000)
            appointment.save()
            appointment.service_id.set(selected_services)

            return redirect("all_doctors_services")
    else:
        form = AppointmentForm()
    current_year = datetime.today().year
    data = {'current_year': current_year, 'form': form}
    return render(request, 'appointments/appointmentForm.html', data)


def doctor_info(request, doctor_slug):
    doctor = Doctors.objects.get(doctor_slug=doctor_slug)
    data = {'doctor': doctor}
    return render(request, 'appointments/doctorInfo.html', data)