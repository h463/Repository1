from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Room(models.Model):
    rno = models.IntegerField()
    ac_rno = models.IntegerField()
    vip_rno = models.IntegerField()

    def __str__(self):
        return str(self.rno)

class Customer(models.Model):
    name = models.ForeignKey(User, related_name='name', on_delete=models.DO_NOTHING)
    phno = models.IntegerField()
    email = models.EmailField()
    govtid = models.CharField(max_length=64)
    purpose = models.CharField(max_length=256)
    checkin = models.DateField()
    checkout = models.DateField()

    def __str__(self):
        return str(self.name)