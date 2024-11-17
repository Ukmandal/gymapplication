from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def manager(request):
    manager = [{ 
        'manager_name': 'Manager', 
    }]

    return HttpResponse(manager)