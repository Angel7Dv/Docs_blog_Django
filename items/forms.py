from django import forms
from .models import Category, Tema, Article

class AddNewCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields =( 'name','ordering')


class AddNewTema(forms.ModelForm):
    class Meta:
        model = Tema
        fields =( 'name','ordering','category')



class AddNewArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields =( 'title','ordering','tema', 'body')