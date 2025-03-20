from django.views.generic import View, TemplateView, CreateView, FormView, DetailView, ListView


from django.shortcuts import render

# Create your views here.

class HomeView(TemplateView):
    template_name = "home.html"

