from django import forms
from pip._vendor.rich.status import Status

from appointments.models import *


class AppointmentFormAdmin(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ['first_name_p', 'last_name_p','date_start', 'date_end','status_id','date_of_birth', 'phone_number_p', 'doctor_id',
                  'service_id']
        widgets = {

            'doctor_id': forms.Select(attrs={'class': 'form-control'}),
            'patient_id': forms.Select(attrs={'class': 'form-control'}),
            'service_id': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            'first_name_p': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name_p': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'phone_number_p': forms.TextInput(attrs={'class': 'form-control'}),
            'date_start': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'date_end': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),

            'status_id': forms.Select(attrs={'class': 'form-control'}),
        }



class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctors
        fields = ['first_name_d', 'last_name_d', 'info_d', 'img_doctor', 'doctor_slug']


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name_service', 'service_slug']


class StatusForm(forms.ModelForm):
    class Meta:
        model = StatusAppointment
        fields = ['status_name']


class SubserviceForm(forms.ModelForm):
    class Meta:
        model = SubService
        fields = ['name_subservice', 'service_id', 'price', 'subservice_slug']


class ExtendedSearchForm(forms.Form):
    patient_name = forms.CharField(
        max_length=100,
        label="Название книги",
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Введите имя пациента...", "class": "patient_name", 'name': "search_patient_name"}
        ),
    )

    medical_insurance = forms.CharField(
        max_length=100,
        label="Мед полис",
        required=False,
        widget=forms.TextInput(
            {"placeholder": "Введите медицинский полис...", "class": "med_insurance", 'name': "search_med_insurance"}
        ),
    )

    start_date = forms.DateField(
        label="От",
        widget=forms.DateInput(attrs={"type": "date", "class": "start_date", "name": "search_start_date"}),
        required=False,
    )

    end_date = forms.DateField(
        label="До",
        widget=forms.DateInput(attrs={"type": "date", "class": "end_date", "name": "search_end_date"}),
        required=False,
    )


class LogInForm(forms.Form):
    username = forms.CharField(
        max_length=100,

    )
    password = forms.CharField(
        max_length=8,
    )
