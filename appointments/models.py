from django.db import models
from django.urls import reverse
from datetime import datetime, timedelta


class Service(models.Model):
    name_service = models.CharField(max_length=100)
    service_slug = models.SlugField(
        max_length=255, unique=True, db_index=True, default=""
    )

    class Meta:
        verbose_name = 'Сервис'
        verbose_name_plural = 'Сервисы'
        db_table = 'services'

    def __str__(self):
        return self.name_service

    def get_absolute_url(self):
        return reverse(
            "selected_service", kwargs={"service_slug": self.service_slug}
        )


class SubService(models.Model):
    name_subservice = models.CharField(max_length=100)
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE)
    price = models.CharField(max_length=254, default='')
    subservice_slug = models.SlugField(
        max_length=255, unique=True, db_index=True, default=""
    )

    class Meta:
        verbose_name = "Вспомогательный сервис"
        verbose_name_plural = 'Вспомогательные сервисы'
        db_table = 'subservices'

    def __str__(self):
        return self.name_subservice


class Doctors(models.Model):
    first_name_d = models.CharField(max_length=50)
    last_name_d = models.CharField(max_length=50)
    info_d = models.TextField(max_length=500)
    img_doctor = models.ImageField(upload_to="appointments/static/img/team", default="")

    doctor_slug = models.SlugField(
        max_length=255, unique=True, db_index=True, default=""
    )

    class Meta:
        verbose_name = 'Доктор'
        verbose_name_plural = 'Доктора'
        db_table = 'doctors'

    def __str__(self):
        return self.first_name_d

    def get_absolute_url(self):
        return reverse(
            "selected_doctor", kwargs={"doctor_slug": self.doctor_slug}
        )


class StatusAppointment(models.Model):
    status_name = models.CharField(max_length=55)

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
        db_table = 'status'

    def __str__(self):
        return self.status_name



class Appointment(models.Model):
    METHOD_PAY = [("терминал", "Терминал"), ("click", "Click"), ("наличными", "Наличными")]
    STATUS_PAY = [("не оплачено", "Не оплачено"), ("оплачено", "Оплачено")]
    first_name_p = models.CharField(max_length=50, default='')
    last_name_p = models.CharField(max_length=50, default='')
    date_of_birth = models.DateField(blank=True)
    phone_number_p = models.CharField(max_length=9)
    medical_insurance = models.CharField(max_length=9, unique=True, default='')
    date_start = models.DateTimeField(null=True)
    date_end = models.DateTimeField(null=True)
    status_id = models.ForeignKey(StatusAppointment, on_delete=models.SET_NULL, default='', null=True)
    doctor_id = models.ForeignKey(Doctors, on_delete=models.SET_NULL, null=True)

    pay_method = models.CharField(max_length=50, default='', null=True, choices=METHOD_PAY)
    pay_status = models.CharField(max_length=50, default='не оплачено', null=True, choices=STATUS_PAY)
    service_id = models.ManyToManyField(SubService)

    class Meta:
        verbose_name = "Встреча"
        verbose_name_plural = "Встречи"
        db_table = 'appointment'

    def __str__(self):
        return self.doctor_id.first_name_d






