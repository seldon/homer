from django.shortcuts import render_to_response
from django.views.generic.list_detail import object_list

from estates.models import Typology

def home(request):
    promoted_list = []
    for t in Typology.objects.all():
        if t.first_page:
            promoted_list.append(t)
    return render_to_response('estate-home.html', {'promo_typ':promoted_list[:3]})
