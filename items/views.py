from django.shortcuts import render
from items.models import Item


# Create your views here.
def index_page(request):
    items = Item.objects.all()
    return render(request, 'index.html', {'items': items})


