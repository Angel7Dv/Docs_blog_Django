from .models import Category

def navbar_category(request):
    navbar_categories = Category.objects.all().order_by('ordering')
    return {'navbar_categories':navbar_categories}


    