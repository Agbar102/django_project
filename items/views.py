from django.shortcuts import render
from items.models import Category, Subcategory, Item


def get_category(request):
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    return render(request, 'base.html', {'categories': categories, 'subcategories': subcategories})

def about(request):
    return render(request, 'about.html')

def base(request):
    return render(request, 'base.html')


def get_items(lang):
    if lang == "en":
        return Item.objects.filter(is_available=True).values('name_en')

def items_view(request):
    lang = request.GET.get('lang', 'en')
    items = get_items(lang)
    return render(request, 'base.html', {'items': items})




# def company(request):
#     return render(request, 'company.html')
#
