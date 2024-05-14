from django.urls import path

from adminPanel import views as adminPanelViews

urlpatterns = [
    path('', adminPanelViews.get_appointments_admin, name='get_appointments_admin'),
    path('update_meet/<int:id_meet>', adminPanelViews.update_appointments_admin, name='update_meet'),
    path('delete_meet/<int:id_meet>', adminPanelViews.delete_appointments_admin, name='delete_meet'),
    path('add_meet/', adminPanelViews.add_appointments_admin, name='add_meet'),
    path('check/<int:id_meet>', adminPanelViews.printInfo, name='check'),
    path('update_payment_status/<int:id_meet>/', adminPanelViews.update_payment_status, name='update_payment_status'),
    path('export_data/', adminPanelViews.export_excel, name='export_data'),
    path('logout/', adminPanelViews.logout_view, name='logOut'),
    path('login/', adminPanelViews.login_page, name='login_page'),

    path('doctors/', adminPanelViews.get_doctors_admin, name='doctors'),
    path('addDoctors/', adminPanelViews.add_doctors_admin, name='addDoctors'),
    path('delete_doctors/<slug:doctor_slug>', adminPanelViews.delete_doctors_admin, name='delete_doctors'),
    path('update_doctor/<slug:doctor_slug>', adminPanelViews.update_doctors_admin, name='update_doctor'),

    path('services/', adminPanelViews.get_medical_services_admin, name='services'),
    path('delete_services/<slug:service_slug>', adminPanelViews.delete_medical_services_admin, name='delete_services'),
    path('update_services/<slug:service_slug>', adminPanelViews.update_medical_service, name='update_services'),
    path('add_service/', adminPanelViews.add_service_admin, name='add_service'),

    path('status/', adminPanelViews.get_status_admin, name='status'),
    path('add_status/', adminPanelViews.add_status_admin, name='add_status'),
    path('delete_status/<int:id_status>', adminPanelViews.delete_status_admin, name='delete_status'),
    path('update_status/<int:id_status>', adminPanelViews.update_status_admin, name='update_status'),

    path('subservice/', adminPanelViews.get_subservice_admin, name='subservice'),
    path('add_subservie/', adminPanelViews.add_subservice_admin, name='add_subservice'),
    path('delete_subservice/<slug:subservice_slug>', adminPanelViews.delete_subservice_admin, name='delete_subservice'),
    path('update_subservice/<slug:subservice_slug>', adminPanelViews.update_subservice_admin, name='update_subservice'),

]
