from functools import wraps
from django.shortcuts import render
from .models import Order, Product

def home(request):
    return render(request, 'home.html')