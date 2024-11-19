from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Manager


def home(request):
    managers = Manager.objects.all()
    context = {
        'managers': managers
    }
    return render(request, 'manager/home.html', context)

def manager_detail(request, pk):
    manager = get_object_or_404(Manager, pk=pk)
    context = {
        'manager': manager
    }
    return render(request, 'manager/manager_detail.html', context=context)