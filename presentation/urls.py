# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("do-action/", views.do_action, name="do_action"),  # view to call
]
