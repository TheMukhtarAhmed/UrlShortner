import datetime 
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey





# Create your models here.
class Input_URL(models.Model):
    # UserID = models.IntegerField(primary_key=True, unique=True, null=False)
    
    UserID = models.ForeignKey('User', on_delete=CASCADE, related_name="UserID")
    ip_addresss = models.GenericIPAddressField()
    input_url = models.URLField(blank=False)
    shorten_url = models.URLField(blank=False)
    count = models.IntegerField(blank=False)
    CreationDate = models.DateField()
    ExpirationDate = models.DateField()
    
    


    def __str__(self):
        return self.input_url


class User(models.Model):
    
    Name = models.CharField(max_length=20, blank=False, null=False )
    Email = models.EmailField(blank=False, null=False)
    




