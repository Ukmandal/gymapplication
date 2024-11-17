from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def member(request):
    member = [{
        'members_name': 'member', 
    }]

    return HttpResponse(member)