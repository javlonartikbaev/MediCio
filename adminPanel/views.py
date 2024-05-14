from random import randint

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect

from appointments.forms import AppointmentForm
# Create your views here.
from .forms import *


@login_required()
def get_appointments_admin(request):
    search = ExtendedSearchForm(request.GET)
    found_patient = Appointment.objects.order_by('date_start')
    if search.is_valid():
        search_patient_name = search.cleaned_data.get("patient_name")
        search_medical_insurance = search.cleaned_data.get("medical_insurance")
        search_start_date = search.cleaned_data.get("start_date")
        search_end_date = search.cleaned_data.get("end_date")
        if search_patient_name:
            found_patient = found_patient.filter(Q(first_name_p__icontains=search_patient_name) | Q(last_name_p__icontains=search_patient_name))
        if search_medical_insurance:
            found_patient = found_patient.filter(medical_insurance__icontains=search_medical_insurance)
        if search_start_date and search_end_date:
            found_patient = found_patient.filter(
                date_start__range=[search_start_date, search_end_date]
            )
        elif search_start_date:
            found_patient = found_patient.filter(
                date_start__icontains=search_start_date
            )

        data = {'search': search, 'found_patient': found_patient, }

    else:
        appointments = Appointment.objects.order_by('date_start')
        paginator = Paginator(appointments, 4)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        data = {"page_obj": page_obj, }
    return render(request, 'adminPanel/appointments/index.html', data)


@login_required()
def update_appointments_admin(request, id_meet):
    appointment = get_object_or_404(Appointment, pk=id_meet)
    if request.method == 'POST':
        form = AppointmentFormAdmin(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('get_appointments_admin')
    else:
        form = AppointmentFormAdmin(instance=appointment)
        data = {"form": form}
        return render(request, 'adminPanel/appointments/updateMeet.html', data)


@login_required()
def delete_appointments_admin(request, id_meet):
    appointment = get_object_or_404(Appointment, pk=id_meet)
    if request.method == 'POST':
        appointment.delete()
        return redirect('get_appointments_admin')

    return render(request, 'adminPanel/appointments/deleteMeet.html', {'appointment': appointment})


@login_required()
def add_appointments_admin(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            selected_services = form.cleaned_data['service_id']
            appointment.medical_insurance = randint(100000000, 1000000000)
            appointment.save()
            appointment.service_id.set(selected_services)
            return redirect("get_appointments_admin")
    else:
        form = AppointmentForm()

    data = {'form': form}
    return render(request, 'adminPanel/appointments/addMeet.html', data)


@login_required()
def printInfo(request, id_meet):
    appointments = get_object_or_404(Appointment, pk=id_meet)
    total_price = 0
    for service in appointments.service_id.all():
        total_price += int(service.price)

    date = datetime.today().strftime('%d.%m.%Y')
    time = datetime.today().strftime('%H:%M:%S')
    data = {"appointments": appointments, "date": date, 'time': time, 'total_price': total_price}
    return render(request, 'adminPanel/appointments/printInfo.html', data)

@login_required()
def update_payment_status(request, id_meet):
    appointment = get_object_or_404(Appointment, pk=id_meet)

    appointment.pay_status = 'оплачено'
    appointment.save()
    return redirect('get_appointments_admin')


@login_required()
def get_doctors_admin(request):
    doctors = Doctors.objects.all()
    paginator = Paginator(doctors, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {"page_obj": page_obj}
    return render(request, 'adminPanel/doctors/doctors.html', data)


@login_required()
def add_doctors_admin(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('doctors')
    else:
        form = DoctorForm()

    return render(request, 'adminPanel/doctors/addDoctors.html', {'form': form})


@login_required()
def delete_doctors_admin(request, doctor_slug):
    doctor = get_object_or_404(Doctors, doctor_slug=doctor_slug)
    if request.method == 'POST':
        doctor.delete()
        return redirect('doctors')
    return render(request, 'adminPanel/doctors/deleteDoctors.html', {'doctor': doctor})


@login_required()
def update_doctors_admin(request, doctor_slug):
    doctor = get_object_or_404(Doctors, doctor_slug=doctor_slug)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctors')
    else:
        form = DoctorForm()
        data = {"form": form}
        return render(request, 'adminPanel/doctors/updateDoctors.html', data)


@login_required()
def get_medical_services_admin(request):
    appointments = Service.objects.all()
    paginator = Paginator(appointments, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {"page_obj": page_obj}
    return render(request, 'adminPanel/medical_services/medService.html', data)


@login_required()
def delete_medical_services_admin(request, service_slug):
    service = get_object_or_404(Service, service_slug=service_slug)
    if request.method == 'POST':
        service.delete()
        return redirect('services')
    return render(request, 'adminPanel/medical_services/medServiceDelete.html', {'service': service})


@login_required()
def update_medical_service(request, service_slug):
    service = get_object_or_404(Service, service_slug=service_slug)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('services')
    else:
        form = ServiceForm()
    return render(request, 'adminPanel/medical_services/medServiceUpdate.html', {'form': form})


@login_required()
def add_service_admin(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('services')
    else:
        form = ServiceForm()
    return render(request, 'adminPanel/medical_services/medServiceAdd.html', {"form": form})


@login_required()
def get_status_admin(request):
    status = StatusAppointment.objects.all()
    paginator = Paginator(status, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {"page_obj": page_obj}
    return render(request, 'adminPanel/status/status.html', data)


@login_required()
def add_status_admin(request):
    if request.method == "POST":
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('status')
    else:
        form = StatusForm()
    return render(request, 'adminPanel/status/statusAdd.html', {'form': form})


@login_required()
def delete_status_admin(request, id_status):
    status = get_object_or_404(StatusAppointment, pk=id_status)
    if request.method == 'POST':
        status.delete()
        return redirect('status')
    return render(request, 'adminPanel/status/statusDelete.html', {'status': status})


@login_required()
def update_status_admin(request, id_status):
    pass


@login_required()
def get_subservice_admin(request):
    subservice = SubService.objects.all()
    paginator = Paginator(subservice, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {"page_obj": page_obj}
    return render(request, 'adminPanel/subservices/subservice.html', data)


@login_required()
def delete_subservice_admin(request, subservice_slug):
    subservice = get_object_or_404(SubService, subservice_slug=subservice_slug)
    if request.method == 'POST':
        subservice.delete()
        return redirect('subservice')
    return render(request, 'adminPanel/subservices/deleteSubservice.html', {'subservice': subservice})


@login_required()
def update_subservice_admin(request, subservice_slug):
    subservice = get_object_or_404(SubService, subservice_slug=subservice_slug)
    if request.method == 'POST':
        form = SubserviceForm(request.POST, instance=subservice)
        if form.is_valid():
            form.save()
            return redirect('subservice')
    else:
        form = SubserviceForm()
    return render(request, 'adminPanel/subservices/updateDoctors.html', {"form": form})


@login_required()
def add_subservice_admin(request):
    if request.method == 'POST':
        form = SubserviceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subservice')
    else:
        form = SubserviceForm()

    return render(request, 'adminPanel/subservices/subserviceAdd.html', {"form": form})




def logout_view(request):
    logout(request)
    return redirect('login_page')


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/login/')

        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, "Invalid Password")
            return redirect('login_page')
        else:
            login(request, user)
            return redirect('get_appointments_admin')

    return render(request, 'adminPanel/appointments/logIn.html')
