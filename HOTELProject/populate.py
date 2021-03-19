import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HOTELProject.settings')
import django
django.setup()

from hotelapp.models import *
from faker import Faker
from random import *
fake = Faker()
def populate(n):
    for i in range(n):
        frno = randint(101, 110)
        fac_rno = randint(201, 210)
        fvip_rno = randint(301, 310)
        rooms = Room.objects.get_or_create(rno=frno, ac_rno=fac_rno, vip_rno=fvip_rno)
populate(10)

