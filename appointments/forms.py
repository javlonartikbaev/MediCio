from django import forms

from .models import *


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ['first_name_p', 'last_name_p', 'date_of_birth', 'phone_number_p', 'doctor_id',
                  'service_id']
        widgets = {

            'status_id': forms.Select(attrs={'class': 'form-control'}),
            'doctor_id': forms.Select(attrs={'class': 'form-control'}),
            'patient_id': forms.Select(attrs={'class': 'form-control'}),
            'service_id': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            'first_name_p': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name_p': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'phone_number_p': forms.TextInput(attrs={'class': 'form-control'}),
        }




