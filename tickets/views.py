from django.shortcuts import render
from .scrapers import Klook, Kkday


def index(request):

    klook = Klook("花蓮")
    kkday = Kkday("花蓮")
    tickets = klook.scrape() + kkday.scrape()

    context = {
        "tickets": tickets
    }

    return render(request, "tickets/index.html", context)
