from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


class AdminDoctor(admin.ModelAdmin):
    list_display = ('first_name_d', 'last_name_d', 'info_d','img_doctor', 'doctor_slug',)







class AdminService(admin.ModelAdmin):
    list_display = ('name_service', 'service_slug',)


class AdminAppointment(admin.ModelAdmin):
    list_display = ('first_name_p','last_name_p','phone_number_p','date_start', 'date_end', 'status_id', 'get_services', 'doctor_id','medical_insurance')
    filter_horizontal = ('service_id',)

    def get_services(self, obj):
        services_info = [f"{service.name_subservice} - {service.price} сум" for service in obj.service_id.all()]
        return mark_safe("<br>".join(services_info))


class AdminSubservice(admin.ModelAdmin):
    list_display = ('name_subservice', 'service_id', 'price', 'subservice_slug',)


class AdminStatus(admin.ModelAdmin):
    list_display = ('status_name',)


admin.site.register(Doctors, AdminDoctor)

admin.site.register(Service, AdminService)
admin.site.register(SubService, AdminSubservice)
admin.site.register(Appointment, AdminAppointment)
admin.site.register(StatusAppointment, AdminStatus)
