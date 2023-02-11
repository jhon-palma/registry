import datetime
from django.db import models

from .choices import *

class Urbanization(models.Model):
    urbanization = models.CharField(max_length=60)

    def __str__(self):
        return self.urbanization

class Contacts(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    type_document = models.CharField(max_length=2, choices=TYPE_DOCUMENT)
    document = models.CharField(unique=True, max_length=12)
    birthday = models.DateField(null=False)
    gender = models.CharField(max_length=1, choices=GENDER)
    address = models.CharField(max_length=200, blank=True, null=False)
    urbanization = models.ForeignKey(Urbanization,on_delete=models.CASCADE)
    email = models.EmailField()
    cellphone = models.CharField(max_length=15, blank=True, null=False)
    ocupation = models.CharField(max_length=24, choices=OCUPATION)
    skills = models.CharField(max_length=11, choices=SKILLS)
    leader = models.ManyToManyField(Urbanization, through='UrbanizationLeader',blank=True, related_name='urbanization_leader')
    note = models.TextField()

    def getEdad(self):
        return int((datetime.now().date() - self.birthday).days / 365.25)
    
class UrbanizationLeader(models.Model):
    leader = models.ForeignKey(Contacts,on_delete=models.CASCADE, related_name='leaders')
    urbanization = models.ForeignKey(Urbanization,on_delete=models.CASCADE, related_name='urbanizations')

    def __str__(self):
        return self.leader.first_name + ' ' + self.leader.last_name + ' - ' +  self.urbanization.urbanization

    
class Agreements(models.Model):
    date = models.DateField(null=False)
    hour = models.TimeField(null=False)
    type = models.CharField(max_length=30,choices=TYPE_AGREEMENTS) 
    detail = models.TextField()
    leader = models.ForeignKey(UrbanizationLeader, on_delete=models.CASCADE)
    contact = models.TextField()

