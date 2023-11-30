from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone


# Create your views here.
def index(request):
    context = {"articles": []}

    return render(request, "blog/index.html", context)


import random


def hello(request):
    fortune = random.randint(1, 3)
    isGreatFortune = False
    fortuneMessage = ""

    if fortune == 1:
        isGreatFortune = True
        fortuneMessage = "Great Fortune"
    elif fortune == 2:
        fortuneMessage = "Small Fortune"
    else:
        fortuneMessage = "Bad Fortune"

    data = {
        "name": "Alice",
        "weather": "CLOUDY",
        "weather_detail": ["temperature: 23℃", "humidity: 40", "wind: 5m/s"],
        "isGreatFortune": isGreatFortune,
        "fortune": fortuneMessage,
    }
    return render(request, "blog/hello.html", data)


def redirect(request):
    return redirect(hello)


def detail(request, article_id):
    context = {
        "article_id": article_id,
    }
    return render(request, "blog/tbd.html", context)


def update(request, article_id):
    context = {
        "article_id": article_id,
    }
    return render(request, "blog/tbd.html", context)


def delete(request, article_id):
    return redirect(index)
