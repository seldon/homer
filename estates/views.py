from django.shortcuts import render_to_response
from django.views.generic.list_detail import object_list

from estates.models import Typology, Estate

def home(request):
    """
    Build the "homepage" for the Real Estate section.

    Build a dictionary, where each key is a Typology's name, and its value is a 
    list of Estate objects belonging to that Typology.
    Only Typologies and Estates with the "first_page" flag are stored in the
    dictionary. 
    
    Example:
            dictionary = { 
                            'Attico':[obj_estate_11, obj_estate_2],
                            'Villa':[obj_estate_1, obj_estate_9, obj_estate_20],
                            'Monolocale':[obj_estate_12]
                        }     
    """
    promoted = {}

    for types in Typology.objects.all():
        if types.first_page:
            promoted[types.typology] = []
    for promo_types in promoted.keys():
        for estate in Estate.objects.all():
            if (estate.typology.typology == promo_types) and (estate.first_page == True):
                promoted[promo_types].append(estate)

    return render_to_response('estate-home.html', {'promoted':promoted})    






