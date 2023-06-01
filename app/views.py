from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from app.models import *
from django.urls import reverse_lazy

class Home(TemplateView):
    template_name='app/home.html'

class School_List(ListView):
    model=School
    context_object_name='schools'

class SchoolDetail(DetailView):
    model=School
    context_object_name='sclobject'

class Create_School(CreateView):
    model=School
    fields='__all__'

class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'

class SchoolDelete(DeleteView):
    model=School
    context_object_name='sclobject'
    success_url=reverse_lazy('School_List')