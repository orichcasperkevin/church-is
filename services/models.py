from django.db import models
from django.utils import timezone


class ServiceType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    start = models.TimeField(default=timezone.now)
    end = models.TimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Service(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.ForeignKey(ServiceType, on_delete=models.CASCADE, null=True)
    venue = models.CharField(max_length=100, help_text='The day of the service', default="none", null = True)
    date = models.DateField(help_text='The day of the service', default="2019-05-01", null = True)
    start = models.TimeField(help_text='write time e.g 00:22:19', null = True)
    end = models.TimeField(help_text='write time e.g 00:22:19', null = True)

    max_attendance = models.IntegerField(default=100,null=True)

    @property
    def remaining_slots(self):
        max_attendance = self.max_attendance or 0
        return  max_attendance - Booking.objects.filter(service=self).count()


    class Meta:
        ordering = ('-date',)

class ServiceItem(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    action = models.CharField(max_length=100, default="not given",null=True)
    value = models.CharField(max_length=200, default="not given", null=True)

#COVID-19
class Booking(models.Model):
    service = models.ForeignKey(Service,on_delete = models.CASCADE)
    phone_number = models.CharField(max_length=10)
    names = models.CharField(max_length=40)
    waiting = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        '''
            Check if booking is full
        '''
        if self.service.remaining_slots < 0:
            self.waiting = True
        #normal save
        super(Booking, self).save(*args, **kwargs)
