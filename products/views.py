from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def product(request):
    members = [{
        'products_name': 'products', 
    }]

    return HttpResponse(product)