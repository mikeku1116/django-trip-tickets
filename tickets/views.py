from django.shortcuts import render
from .scrapers import Klook, Kkday


def index(request):

    klook = Klook(request.POST.get("city_name"))
    kkday = Kkday(request.POST.get("city_name"))

    context = {
        "tickets": klook.scrape() + kkday.scrape()
    }

    return render(request, "tickets/index.html", context)
