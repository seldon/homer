from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    """
    News related to the "Building administration" section, inserted by
    Belenchia's staff
    """
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    slug = models.SlugField(max_length=200)


    class Meta:
        verbose_name_plural = 'news'
        ordering = ["-date"]


    def __unicode__(self):
        return self.title
    

