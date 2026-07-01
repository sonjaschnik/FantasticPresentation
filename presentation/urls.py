# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('do_action/', views.do_action, name='do_action'),
    path('stocks/', views.stocks, name='stocks'),
    path('readme/', views.readme, name='readme'),
]
