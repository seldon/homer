from django.db import models
from django.utils.safestring import SafeUnicode

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill



class Owner(models.Model):
    """
    This class collect data of the owner of the estate(s). 
    Every Owner can have more than one Estate.
    It is a very simple anagraphic archive.
    """
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __unicode__(self):
        return '%s %s' % (self.last_name, self.first_name)


class Typology(models.Model):
    """
    Typology is the second level of the taxonomy.
    Multiple tipologies belongs to a single Category.
    """
    typology = models.CharField(max_length=200)
    first_page = models.BooleanField(default=False)

    class Meta:
        ordering = ['typology']                
        verbose_name_plural = 'typologies'

    def __unicode__(self):
        return self.typology



class Category(models.Model):
    """
    Category is the first level of the taxonomy.
    Every Category has multiple typologies related.
    """
    category = models.CharField(max_length=200)
    typology = models.ManyToManyField(Typology)

    class Meta:
        ordering = ['category']
        verbose_name_plural = 'categories'

    def __unicode__(self):
        return self.category



class Estate(models.Model):
    """
    The common model for all the estate data.
    Every Estate has a single Typology.  
    """
    SELLING_TYPE = (
        ('SALE', 'vendita'),
        ('RENT', 'affitto'),
    )

    #name = models.CharField(max_length=30) # Useless ???
    address = models.CharField(max_length=200)
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
        return '%s - %s' % (self.address, self.owner)

    @models.permalink
    def get_absolute_url(self):
        return ('detail_single_estate', [str(self.id)])



class EstateImage(models.Model):
    """
    Images for the estates.
    Every Estate can have more than one EstateImage (and should have at least ONE).
    The first image for every estate (i.e., the image with the smallest 'position' value)
    is considered the 'front image' for that Estate.
    """
    estate = models.ForeignKey(Estate, related_name='images')
    position = models.PositiveSmallIntegerField()
    original = models.ImageField(upload_to='images')
    thumbnail = ImageSpecField([ResizeToFill(160, 90)], image_field='original', format='JPEG', options={'quality':90})

    def admin_thumb(self):
        return SafeUnicode('<img src="'+str(self.thumbnail.url)+'" />');

    class Meta:
        ordering = ['estate', 'position']

    def __unicode__(self):
        return SafeUnicode('<img src="' + str(self.thumbnail.url) + '" />')
        
