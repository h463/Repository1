# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from recipe_app.models import Recipes
from rest_framework.response import Response
# Create your views here.

class Recipes(APIView):
    def get(self,request):
       rec =Recipes.objects.value_list("id", "name")
       return Response(rec)

    def post(self,request):
        rec =Recipes.objects.get(id=request.post["id"])
        rec.name =request.post["name"]
        rec.save()
        return Response(rec)

