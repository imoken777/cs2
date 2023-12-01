from django.http import HttpResponse
from django.shortcuts import render


def root(request):
    return HttpResponse("Hello, world!")


# Create your views here.
def pattern(request, username):
    return HttpResponse("Hello {}".format(username))


def param(request):
    text = ""
    for key in request.GET:
        text += "{} : {}, ".format(key, request.GET[key])
    return HttpResponse(text)
