# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from recipe_app.models import Recipes
# Create your models here.

from django.forms import ModelForm
from .models import Recipe


class Recipes(ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'