from django.shortcuts import render
from .models import *


# Create your views here.
def home(request):
    hero = Hero.objects.latest('id')
    about = About.objects.latest('id')
    service_title = ServiceTitle.objects.latest('id')
    service = Service.objects.all()
    client_title = OurClientTitle.objects.latest('id')
    client_logo = OurClientLogo.objects.all()
    contact = Contact.objects.latest('id')
    our_value = OurValue.objects.all()
    our_value_title = OurValueTitle.objects.latest('id')
    feature_title = FeatureTitle.objects.latest('id')
    feature = Feature.objects.all()
    faq = Faq.objects.all()
    faq_list1 = faq[:len(faq) // 2]
    faq_list2 = faq[len(faq) // 2:]

    return render(request, "index.html", {
        "hero": hero,
        "about": about,
        "service_title": service_title,
        "service": service,
        "client_title": client_title,
        "client_logo": client_logo,
        "contact": contact,
        "our_value": our_value,
        "our_value_title": our_value_title,
        "feature_title": feature_title,
        "feature": feature,
        "faq": faq,
        "faq_list1": faq_list1,
        "faq_list2": faq_list2
    })


def read_more_hero(request):
    hero = Hero.objects.latest('id')
    return render(request, "index_more.html", {
        "more_hero": hero
    })


def read_more_about(request):
    about = About.objects.latest('id')
    return render(request, "index_more.html", {
        "more_about": about
    })


def read_more_service(request, pk):
    service = Service.objects.get(id=pk)
    return render(request, "index_more.html", {
        "more_service": service
    })
