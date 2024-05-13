from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from appointments import views as appointment_views

urlpatterns = [
    path('', appointment_views.all_doctors_services, name='all_doctors_services'),
    path('appointment/', appointment_views.appointment_form, name='appointment_form'),
    path('doctorInfo/<slug:doctor_slug>', appointment_views.doctor_info, name='doctor_info'),

]
