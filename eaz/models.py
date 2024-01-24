from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)


class Thing(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    link = models.URLField()
    

class Image(models.Model):
    image = models.ImageField(upload_to='image')
    thing = models.ForeignKey(Thing,on_delete=models.CASCADE,related_name='images')
    