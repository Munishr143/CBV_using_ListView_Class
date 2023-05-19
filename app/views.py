from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView
from app.models import *

class Home(TemplateView):
    template_name='app/home.html'

class School_List(ListView):
    model=School
    context_object_name='schools'
