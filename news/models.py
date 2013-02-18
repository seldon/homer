from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    """
    News related to the "Building administration" section, inserted by
    Belenchia's staff
    """
    title = models.CharField(max_length=30)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    class Meta:
        verbose_name_plural = 'news'

    def __unicode__(self):
        return self.title

