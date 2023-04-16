from django.db import models


# Create your models here.

class Formulaire(models.Model):
    prenom = models.CharField(max_length=40,default="",null=True )
    email = models.EmailField(max_length=100, default="",null=True)
    montant = models.IntegerField(null=True)
    image = models.ImageField(upload_to='photos', default=None, null=True)