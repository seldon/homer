from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from estates.models import Category, Estate, Typology
from estates.forms import SearchForm



def home_estates(request):
    """
    Build the "homepage" for the Real Estate section.

    1 - Initialize the search form with default values.

    2 - Build a dictionary, where each key is a Typology's name, and its value is a 
        list of lists (each of these "2nd-level list" has two elements: an Estate object belonging 
        to that Typology and an EstateImage object which is the thumbnail of the Estate object).

        NOTE:   The thumbnail for an Estate is simply the first element of the list of images related to that Estate.
                (See the EstateImage class in estates/models.py for further information).

        Only Typologies and Estates with the "first_page" flag are stored in the dictionary.
        Typology and Estates are limited in number, to help the template's rendering of the contents. 
    
    Example:
            dictionary = {
                    'Attico':[
                                [obj_Estate_11, thumbnail_obj_Estate_11],
                                [obj_Estate_2, thumbnail_obj_Estate_2],
                            ]
                    'Villa':[
                                [obj_Estate_1, thumbnail_obj_Estate_1],
                                [obj_Estate_9, thumbnail_obj_Estate_9],
                                [obj_Estate_20, thumbnail_obj_Estate_20],
                            ]
                    'Monolocale':[
                                    [obj_Estate_12, thumbnail_obj_Estate_12],
                                ]
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
                if estate.images.count() == 0:  # checks if the Estate object has at least one EstateImage object related
                    thumbnail = ''
                else:
                    thumbnail = estate.images.order_by('position')[0]   # see the NOTE in this function's docstring
                promoted[promo_types].append([estate, thumbnail])   # appends an Estate object and the Estate's thumbnail to the current dictionary's key
                if len(promoted[promo_types]) == ESTATES_MAX_NUMBER:
                    break

    return render_to_response('estate-home.html', {'promoted':promoted, 'form':form}, RequestContext(request))    



def search_estates(request):
    """
    Search in the database all the estates that match with the search criteria, and return them to the template.
    """
    estates_list = []
    
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



def detail_single_estate(request, pk):
    """
    Try to get an Estate object which primary key is passed via the URL pattern.
    Return a "404 - page not found" if no Estate is found.
    """
    estate = get_object_or_404(Estate, pk=pk)
    return render_to_response('estate_detail.html', {'estate':estate}, RequestContext(request))   

