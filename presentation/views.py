# myapp/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse


def home(request):
    return render(request, "home.html")


def do_action(request):
    if request.method == "POST":
        # my server-side logic here
        print("Button clicked! Performing action...")
        return HttpResponse("Action completed successfully!")
    else:
        return redirect("home")  # prevent GET access
