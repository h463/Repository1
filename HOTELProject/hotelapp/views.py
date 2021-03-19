from django.shortcuts import render
from hotelapp.forms import CustomerForm, DetailsForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Room
# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def category_view(request):
    return render(request, 'roomtype.html')
@login_required()
def normal_rooms_view(request):
    rooms = Room.objects.all().order_by('rno')
    return render(request, 'normal_rooms.html', {"rooms":rooms})
@login_required()
def ac_rooms_view(request):
    rooms = Room.objects.all().order_by('ac_rno')
    return render(request, 'ac_rooms.html', {"rooms":rooms})
@login_required()
def vip_rooms_view(request):
    rooms = Room.objects.all().order_by('vip_rno')
    return render(request, 'vip_rooms.html', {"rooms":rooms})

def signup_view(request):
    form = CustomerForm()
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/accounts/login/')
    return render(request, 'signup.html',{"form":form})

def customer_detail_view(request):
    form = DetailsForm()
    if request.method == "POST":
        form = DetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'thank.html')
    return render(request, 'detail.html', {"form":form})

def logout_view(request):
    return render(request,'logout.html')

