from django.db import models
from django.db.models import CharField, EmailField, IntegerField, TextField



# Create your models here.

class Customers(models.Model):
    name = CharField(max_length=70)
    email = EmailField(max_length=255)
    age = IntegerField()


class Article(models.Model):
    id = IntegerField(auto_created=True,unique=True,primary_key=True)
    title = CharField(max_length=255)
    description = TextField(null=False)
    picture = models.ImageField(upload_to= "pictures")
