
from django.shortcuts import render
from items.services import TemplateService

def get_category(request):
    data = TemplateService()
    categories = data.get_category()
    items = data.get_items()

    sub_categories = {}
    for category in categories:
        sub_categories[category.id] = data.get_subcategory(category.id)

    footers = data.get_footer()
    contacts = data.get_contacts()

    context = {
        'categories': categories,
        'sub_categories': sub_categories,
        'items': items,
        'footers': footers,
        'contacts': contacts,
    }
    return render(request, 'base.html', context)


