from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.db import models
from django.contrib.flatpages.models import FlatPage

def home(request):
    DEFAULT_ESTATES_HOME = "estates_home/"
    DEFAULT_ADMINISTRATOR_HOME = "administration_home/"
    DEFAULT_SUMMER_RENT_HOME = "summer_rent_home/"
    
    estates_flatpage = FlatPage.objects.get(url="/%s" % DEFAULT_ESTATES_HOME)
    administrator_flatpage = FlatPage.objects.get(url="/%s" % DEFAULT_ADMINISTRATOR_HOME)
    summer_rent_flatpage = FlatPage.objects.get(url="/%s" % DEFAULT_SUMMER_RENT_HOME)

    
    context = {'estates_flatpage' : estates_flatpage, 
               'administrator_flatpage' : administrator_flatpage,
               'summer_rent_flatpage' : summer_rent_flatpage, }
    return render_to_response('home.html', context_instance=RequestContext(request, context))
