
from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

from common.models import Footer
# Register your models here.

@admin.register(Footer)
class FooterAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass

