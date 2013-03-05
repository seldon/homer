from django import forms
from django.forms.widgets import CheckboxSelectMultiple

from estates.models import Category, Typology

class SearchForm(forms.Form):
    """
    Search form for the estates (they are in models.Estate), able to choice among the categories and the typologies of estates.

    TODO: Decide the class of the fields (now they are all "CharField", but maybe "ChoiceField" is better?) and set REAL initial values (now, they are "ready-to-search" mock values)
    """ 
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Categoria', empty_label=None)
    typology = forms.ModelMultipleChoiceField(queryset=Typology.objects.all(), widget=CheckboxSelectMultiple, label='Tipologia')
    price_min = forms.CharField(required=False, label='Prezzo min', initial=0)
    price_max = forms.CharField(required=False, label='Prezzo max', initial=1000000)
    surface_min = forms.CharField(required=False, label='Superficie min', initial=0)
    surface_max = forms.CharField(required=False, label='Superficie max', initial=10000)
    rooms = forms.CharField(required=False, label='Locali', initial=0)
    bathrooms = forms.CharField(required=False, label='Bagni', initial=0)
    park_slots = forms.CharField(required=False, label='Posti auto', initial=0)

    
    # Override the form's __init__ method to accept an extra optional custom keyword argument: "typologies_list"
    def __init__(self, *args, **kwargs):
        typologies_list = kwargs.pop('typologies_list', None)

        super(SearchForm, self).__init__(*args, **kwargs)

        # if "typologies_list" argument is passed to SearchForm constructor, 
        # limit the queryset of "typology" field to only the typologies specific to a single category
        # (the limited queryset is provided by the "typologies_list" keyword argument).
        if typologies_list:
            self.fields['typology'].queryset = typologies_list      

