from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('<slug:slug>/', categories, name="category"),
    path('<slug:category_slug>/<slug:slug>/', article, name="article"),

    #CRUD add
    path('+add_new_category/', add_new_category, name="add_new_category"),
    path('+add_new_tema/', add_new_tema, name="add_new_tema"),
    path('+add_new_article/', add_new_article, name="add_new_article"),

    #EDIT
    path('+edit_category/<slug:slug>/', edit_category, name="edit_category"),
    path('+edit_tema/<slug:slug>/', edit_tema, name="edit_tema"),
    path('+edit_article/<slug:slug>/', edit_article, name="edit_article"),

    #DELETE
    path('+delete_category/<slug:slug>/', delete_category, name="delete_category"),
    path('+delete_tema/<slug:slug>/', delete_tema, name="delete_tema"),
    path('+delete_article/<slug:slug>/', delete_article, name="delete_article"),

    

    
]
