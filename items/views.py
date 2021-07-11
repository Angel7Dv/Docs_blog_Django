from django.shortcuts import render, get_object_or_404
from .models import Category, Tema, Article
# Create your views here.

def categories(request, slug):
    category = get_object_or_404(Category, slug=slug)
    temas = category.temas.all()
    

    #cosita = temas[0].articles #forma de sacarle los articulos
    #print('temas ========>', temas )
    #print('EXPERIMENTO', cosita)
    #for i in temas:
        #art = i.articles.all()
        #print('articulos ========>', art )


    ctx = {
        'category': category,
        'temas':temas,           
    }
    return render(request, 'items/category.html', ctx)

def article(request,category_slug, slug):
    article = get_object_or_404(Article, slug=slug)
    category = get_object_or_404(Category, slug=category_slug)
    temas = category.temas.all()
    
    #article.tema = tema actual
    #temas[0].articles.all() todos los articulos del tema0
    # article.tema.articles.all() todos los articulos del tema actual

    # article.tema.articles.filter(title=article.title)

    

    ctx = {
        'article':article,
        'category': category,
        'temas':temas, 
    }
    return render(request, 'items/article.html', ctx)

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import AddNewCategory, AddNewTema, AddNewArticle


#ADD CATEGORY
@login_required
def add_new_category(request):

    if request.method == 'POST':      
        form = AddNewCategory(request.POST)   
        if form.is_valid():                 
            form.save()                                          
            return redirect('index')
    else:                        
        form = AddNewCategory()
    ctx = {
        'form': form
    }
    return render(request, 'items/CRUD_Tag.html', ctx)

#EDIT CATEGORY

@login_required
def edit_category(request, slug):

    objeto = Category.objects.get(slug=slug)    

    if request.method == 'GET':         
        form = AddNewCategory(instance=objeto)       #funciona normalmente como un form solo que esta ves  instanciamos sobre el objeto
    else:
        form = AddNewCategory(request.POST, instance=objeto)  #como el if no es POST aqui funciona contrario a lo anterior el else es el que guarda el objeto
        if form.is_valid():
            form.save()
        return redirect('index')

    ctx = {
        'form': form,
        'objeto':objeto
    }

    return render(request, 'items/CRUD_Tag.html', ctx)

#DELETE
@login_required
def delete_category(request, slug):                    #==obtiene dos parametros, la url y el id 
    objeto = Category.objects.get(slug=slug)     #calsifica los objetos por su y sleeciona el objeto actual por su id
    if request.method == 'POST':      
        objeto.delete()                    #borra el id actual
        return redirect('index')
    return render(request, 'items/delete.html', {'objeto':objeto})




#ADD TEMA
@login_required
def add_new_tema(request):

    if request.method == 'POST':      
        form = AddNewTema(request.POST)   
        if form.is_valid(): 
            print('ANTES', form)                   
            form.save()    
            print('SALVADO', form)          
            return redirect('index')
    else:                        
        form = AddNewTema()

    ctx = {
        'form': form
    }

    return render(request, 'items/CRUD_Tag.html', ctx)


#EDIT TEMA

@login_required
def edit_tema(request, slug):
    objeto = Tema.objects.get(slug=slug)    
    if request.method == 'GET':         
        form = AddNewTema(instance=objeto)       #funciona normalmente como un form solo que esta ves  instanciamos sobre el objeto
    else:
        form = AddNewTema(request.POST, instance=objeto)  #como el if no es POST aqui funciona contrario a lo anterior el else es el que guarda el objeto
        if form.is_valid():
            form.save()
        return redirect('index')
    ctx = {
        'form': form,
        'objeto':objeto
    }
    return render(request, 'items/CRUD_Tag.html', ctx)


#DELETE
@login_required
def delete_tema(request, slug):  
                      #==obtiene dos parametros, la url y el id 
    objeto = Tema.objects.get(slug=slug)     #calsifica los objetos por su y sleeciona el objeto actual por su id
    print(objeto)
    if request.method == 'POST':      
        objeto.delete()                    #borra el id actual
        return redirect('index')
    return render(request, 'items/delete.html', {'objeto':objeto})



#Article
#ADD
@login_required
def add_new_article(request):

    if request.method == 'POST':      
        form = AddNewArticle(request.POST)   
        if form.is_valid():                             
            form.save()                      
            return redirect('index')
    else:                        
        form = AddNewArticle()

    ctx = {
        'form': form
    }

    return render(request, 'items/CRUD_Tag.html', ctx)

#EDIT ARTICLE
@login_required
def edit_article(request, slug):
    objeto = Article.objects.get(slug=slug)    
    if request.method == 'GET':         
        form = AddNewArticle(instance=objeto)       #funciona normalmente como un form solo que esta ves  instanciamos sobre el objeto
    else:
        form = AddNewArticle(request.POST, instance=objeto)  #como el if no es POST aqui funciona contrario a lo anterior el else es el que guarda el objeto
        if form.is_valid():
            form.save()
        return redirect('index')
    ctx = {
        'form': form,
        'objeto':objeto
    }
    return render(request, 'items/CRUD_Tag.html', ctx)

@login_required
def delete_article(request, slug):          #   obtiene dos parametros, la url y el id                                         
    objeto = Article.objects.get(slug=slug) #   calsifica los objetos por su y sleeciona el objeto actual por su id
    if request.method == 'POST':      
        objeto.delete()                     #   borra el id actual
        return redirect('index')
    return render(request, 'items/delete.html', {'objeto':objeto})