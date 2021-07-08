from django.contrib import admin
from .models import *
# Register your models here.


from tinymce.widgets import TinyMCE
from django.db import models

class ArticleAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: { 'widget': TinyMCE()}
    }

admin.site.register(Category)
admin.site.register(Tema)
admin.site.register(Article, ArticleAdmin)