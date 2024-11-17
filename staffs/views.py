from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def staff(request):
    members = [{
        'staffs_name': 'staff', 
    }]

    return HttpResponse(staff)