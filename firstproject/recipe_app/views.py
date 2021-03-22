# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from recipe_app.models import Recipe, MyUser
from .forms import RecipeForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_view(request):
    #import pdb; pdb.set_trace()
    if request.method == "POST":
        user = authenticate(email=request.POST['email'],
                            password=request.POST['password'])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/recipe_app/home/')
        else:
            return render(request, "login.html", {"error": "Invalid_Credentials"})
    return render(request, "login.html")


def register(request):
    if request.method == "POST":
        MyUser.objects.create_user(email=request.POST["email"],
                                   password=request.POST["password"],
                                   date_of_birth=request.POST["date_of_birth"])
        return HttpResponseRedirect("/recipe_app/")
    return render(request,"register.html")

@login_required(login_url='/recipe_app/')
def home(request):
    recipes = Recipe.objects.order_by('-id')
    return render(request, "home.html", {"recipes": recipes})

@login_required(login_url='/recipe_app/')
def create(request):
    return render(request, "create_recipe.html")


def save_recipe(request):
    recipe_form=RecipeForm(request.POST,  request.FILES)
    if recipe_form.is_valid():
        recipe_form.save()
    else:
        return render(request,"create_recipe.html", {"error":recipe_form.errors})

    return HttpResponseRedirect("/recipe_app/")


@login_required(login_url='/recipe_app/')
def detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, "detail.html", {"recipe": recipe})


@login_required(login_url='/recipe_app/')
def delete(request, recipe_id):
    Recipe.objects.get(id=recipe_id).delete()
    return HttpResponseRedirect('/recipe_app/')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/recipe_app/")

