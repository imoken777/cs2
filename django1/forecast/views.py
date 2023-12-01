import random

from django.shortcuts import render

# Create your views here.
weather = ["Sunny", "Rainy", "Cloudy", "Snowy"]


def index(request):
    params = {}
    params["title"] = "3 days forecast"
    params["forecasts"] = random.choices(weather, k=3)
    return render(request, "forecast/index.html", params)
