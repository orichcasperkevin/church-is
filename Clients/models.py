from django.db import models
from tenant_schemas.models import TenantMixin

class Client(TenantMixin):
    #name is the name of the church
    name = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    paid_until =  models.DateField()
    on_trial = models.BooleanField()
    auto_create_schema = True

    def __str__(self):
        return self.name

class ClientDetail(models.Model):
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    #responsible person
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    ID_number = models.CharField(max_length=8)
    phone_number = models.CharField(max_length=15)
    #church detail.
    city_or_town = models.CharField(max_length=20)
    road_or_street = models.CharField(max_length=20)
    location_description = models.CharField(max_length=100)
    #Contact
    website = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return str(self.client)
