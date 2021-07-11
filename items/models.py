from django.db import models

# Create your models here.
from django.utils.text import slugify



class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50,null=True, blank=True, unique=True)
    ordering = models.IntegerField(null=True, blank=True)
    
    class Meta:
        ordering = ['ordering']

    def save(self, *args, **kwargs):    #luego agregamos esta funcion a la clase para que se agrege el titulo como slug
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Tema(models.Model):  
    category = models.ForeignKey(Category, related_name='temas', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50,null=True, blank=True)
    ordering= models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['ordering']

    def save(self, *args, **kwargs):    #luego agregamos esta funcion a la clase para que se agrege el titulo como slug
        self.slug = slugify(self.name)
        super(Tema, self).save(*args, **kwargs) # == > importante

    def __str__(self):
        return self.name


class Article(models.Model):
    tema = models.ForeignKey(Tema, related_name='articles', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=50,null=True, blank=True,default="name")
    ordering = models.IntegerField(null=True, blank=True,)

    body = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['ordering']

    def save(self, *args, **kwargs):    #luego agregamos esta funcion a la clase para que se agrege el titulo como slug
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs) # == > importante

    def __str__(self):
        return self.title