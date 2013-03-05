from django.db import models

# Create your models here.
class Content(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    block_name = models.CharField(max_length=300,unique)


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()   