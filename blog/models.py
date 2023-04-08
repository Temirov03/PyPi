from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=400)
    photo = models.ImageField(upload_to="blog/images/")
    short_discription = models.TextField()
    discription = RichTextField(null=True, blank=True)