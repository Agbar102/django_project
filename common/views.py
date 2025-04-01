
from django.shortcuts import render
from .models import Contacts

def contacts_view(request):
    contacts = Contacts.get_solo()
    return render(request, 'base.html', {'contacts': contacts})

def get_common():
    common = Contacts.get_solo()
    print(common)