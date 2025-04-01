from django.urls import path
from items.views import get_category

front_urlpatterns = [
    path('', get_category, name='category'),
]


