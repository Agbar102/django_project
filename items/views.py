from django.shortcuts import render
from items.models import Category





def get_category(request):
    items = Category.objects.all()
    return render(request, 'base.html', {'items': items})

