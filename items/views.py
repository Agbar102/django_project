from django.shortcuts import render
from items.models import Item, Banner




# Create your views here.
def index_page(request):
    items = Item.objects.all()
    return render(request, 'index.html', {'items': items})

def banner_view(request):
    banners = Banner.objects.all()
    return render(request, 'index.html',{'banners': banners})


