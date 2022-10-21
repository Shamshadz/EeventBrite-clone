from django.db import models
from traitlets import default
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    image = models.ImageField(null=True,blank=True)
    

class Like(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    event = models.ForeignKey(Event,on_delete=models.SET_NULL,null=True)
    is_liked = models.BooleanField(default=False)
