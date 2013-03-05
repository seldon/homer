from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from estates.models import Category, Estate, Typology
from estates.forms import SearchForm



def home(request):
    """
    Build the "homepage" for the Real Estate section.

    1 - Initialize the search form with default values.

    2 - Build a dictionary, where each key is a Typology's name, and its value is a 
    list of Estate objects belonging to that Typology.
    Only Typologies and Estates with the "first_page" flag are stored in the
    dictionary.
    Typology and Estates are limited in number, to help the template's rendering
    of the contents. 
    
    Example:
            dictionary = {
                    'Attico':[obj_estate_11, obj_estate_2],
                    'Villa':[obj_estate_1, obj_estate_9, obj_estate_20],
                    'Monolocale':[obj_estate_12]
            }     
    """
    # 1 - "Search Form"
    DEFAULT_CATEGORY = 'residenziale'   # the default category when the page is loaded for the first time

    initial_category = Category.objects.get(category__iexact=DEFAULT_CATEGORY)

    form = SearchForm(typologies_list=initial_category.typology.all(), initial={'category':initial_category})   # builds and stores the search form, ready to be passed to the template


    # 2 - "First-page elements dictionary"
    TYPOLOGIES_MAX_NUMBER = 3
    ESTATES_MAX_NUMBER = 5

    promoted = {}

    for types in Typology.objects.all():
        if types.first_page:
            promoted[types.typology] = []
            if len(promoted.keys()) == TYPOLOGIES_MAX_NUMBER:
                break

    for promo_types in promoted.keys():
        for estate in Estate.objects.all():
            if (estate.typology.typology == promo_types) and (estate.first_page == True):
                promoted[promo_types].append(estate)
                if len(promoted[promo_types]) == ESTATES_MAX_NUMBER:
                    break

    return render_to_response('estate-home.html', {'promoted':promoted, 'form':form}, RequestContext(request))    



def search(request):
    """
    Search in the database all the estates that match with the search criteria, and return them to the template.
    """
    estates_list = ''
    
    if request.POST:
        categ = Category.objects.get(id=request.POST['category'])
        form = SearchForm(request.POST, typologies_list=categ.typology.all())
        if form.is_valid():
            estates_list = Estate.objects.filter(
                typology__id__in=form.cleaned_data['typology']
            ).filter(
                rooms__gte=form.cleaned_data['rooms']
            ).filter(
                surface__range=(form.cleaned_data['surface_min'], form.cleaned_data['surface_max'])
            ).filter(
                bathrooms__gte=form.cleaned_data['bathrooms']
            ).filter(
                park_slots__gte=form.cleaned_data['park_slots']
            ).filter(
                price__range=(form.cleaned_data['price_min'], form.cleaned_data['price_max']))

        return render_to_response('search-result.html', {'estates':estates_list, 'form':form}, RequestContext(request))



def ajax_magic(request):
    """
    This function is called when the selected Category in the search form is changed.
    Builds a custom formatted string with the ID and the name of the Typologies related to the new selected Category.
    The custom string is then passed back to the javascript function that made the AJAX request.

    Example:
            string = '1:Villa-3:Attico-8:Bar-5:Appartamento'
         
    """
    t_support_list = []
    categ = Category.objects.get(id=request.POST['category'])
    for t in categ.typology.all():
        support_var = '%s:%s' % (t.id, t.typology)        
        t_support_list.append(support_var)

    types_list = '-'.join(t_support_list)

    return HttpResponse(types_list)

