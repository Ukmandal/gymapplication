from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pk>/', views.manager_detail, name='manager_detail')
]
