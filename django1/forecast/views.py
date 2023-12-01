import random

from django.shortcuts import render

# Create your views here.
weather = ["Sunny", "Rainy", "Cloudy", "Snowy"]


def index(request):
    params = {}
    params["title"] = "7 days forecast"
    params["forecasts"] = random.choices(weather, k=7)
    return render(request, "forecast/index.html", params)
