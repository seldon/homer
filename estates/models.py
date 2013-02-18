from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=30)

    def __unicode__(self):
        return '%s %s' % (self.last_name, self.first_name)

    class Meta:
        ordering = ['last_name', 'first_name']



class Category(models.Model):
    category = models.CharField(max_length=30)

    class Meta:
        ordering = ['category']
        verbose_name_plural = 'categories'

    def __unicode__(self):
        return self.category



class Typology(models.Model):
    """
    WRITE-ME
    (Must decide if Typology class has a one-to-many or many-to-many relationship
    with Estate class)
    """
    typology = models.CharField(max_length=30)
    first_page = models.BooleanField(default=False)

    class Meta:
        ordering = ['typology']                
        verbose_name_plural = 'typologies'

    def __unicode__(self):
        return self.typology



class Estate(models.Model):
    """
    The common model for all the estate data. The different categories (that in
    the site have different sections) are distinguished in the "category" field.  
    """
    name = models.CharField(max_length=30)
    surface = models.PositiveIntegerField(help_text="metri quadri")
    rooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    park_slots = models.PositiveIntegerField()
    price = models.PositiveIntegerField(help_text="euro")
    first_page = models.BooleanField(default=False)
    customer = models.ForeignKey(Customer)
    category = models.ForeignKey(Category)
    # must decide if Typology is a "ManyToMany" or "ForeignKey" field
    #typology = models.ManyToManyField(Typology)

    def __unicode__(self):
        return self.name

