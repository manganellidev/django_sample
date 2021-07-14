from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse


def welcome(request):
    return HttpResponse("Welcome to the Meeting Planner!")


def date(request):
    return HttpResponse(f"This page was server at {str(datetime.now())}")


def about(request):
    return HttpResponse(f"Hello, my name is Wagner, and I'm a software developer!")
