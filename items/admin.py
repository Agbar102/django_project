from django.contrib import admin
from django.contrib.admin import TabularInline
from adminsortable2.admin import SortableAdminMixin

from .models import Item, Category, Subcategory, Characteristic, User, Banner

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    pass

class CharacteristicInline(TabularInline):
    model = Characteristic


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Item)
class ItemAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [CharacteristicInline, ]


@admin.register(Subcategory)
class Subcategory(SortableAdminMixin, admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass

# @admin.register(Contacts)
# class ContactsAdmin(SortableAdminMixin, admin.ModelAdmin):
#     pass

# admin.site.register(Item, ItemAdmin)

