from itertools import product
from re import template
from django.shortcuts import render

# Import views
from django.views.generic import ListView, DetailView
#models
from App_Shop.models import Product
#mixin
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class Home(ListView):
    model = Product
    template_name = 'App_shop/home.html'

class Productdetail(LoginRequiredMixin,DetailView):
    model = Product
    template_name = 'App_Shop/product_detail.html'