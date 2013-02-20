from django.db import models

class Owner(models.Model):
    """
    This class collect data of the owner of the estate(s). 
    Every owner could have more than one estate.
    It is a very simple anagraphic archive.
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=30)

    def __unicode__(self):
        return '%s %s' % (self.last_name, self.first_name)

    class Meta:
        ordering = ['last_name', 'first_name']



class Typology(models.Model):
    """
    Typology is the second level of the taxonomy.
    Multiple tipologies belongs to a single Category.
    """
    typology = models.CharField(max_length=30)
    first_page = models.BooleanField(default=False)

    class Meta:
        ordering = ['typology']                
        verbose_name_plural = 'typologies'

    def __unicode__(self):
        return self.typology



class Category(models.Model):
    """
    Category is the first level of the taxonomy.
    Every category has multiple typologies related.
    """
    category = models.CharField(max_length=30)
    typology = models.ManyToManyField(Typology)

    class Meta:
        ordering = ['category']
        verbose_name_plural = 'categories'

    def __unicode__(self):
        return self.category



class Estate(models.Model):
    """
    The common model for all the estate data.
    Every estate has a single typology.  
    """
    SELLING_TYPE = (
        ('SALE', 'vendita'),
        ('RENT', 'affitto'),
    )

    #name = models.CharField(max_length=30) # Useless ???
    address = models.CharField(max_length=30)
    surface = models.PositiveIntegerField(help_text="metri quadri")
    rooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    park_slots = models.PositiveIntegerField()
    price = models.PositiveIntegerField(help_text="euro")
    first_page = models.BooleanField(default=False)
    selling_type = models.CharField(max_length=4, choices=SELLING_TYPE)
    owner = models.ForeignKey(Owner)
    typology = models.ForeignKey(Typology)

    def __unicode__(self):
        return '%s - %s' % (self.owner, self.address)

