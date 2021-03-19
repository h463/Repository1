from django.contrib import admin
from .models import Room, Customer
from django import forms
# Register your models here.
class RoomAdmin(admin.ModelAdmin):
    list_display= ['rno','ac_rno', 'vip_rno']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phno', 'email', 'checkin', 'checkout']

admin.site.register(Room,RoomAdmin)
admin.site.register(Customer, CustomerAdmin)