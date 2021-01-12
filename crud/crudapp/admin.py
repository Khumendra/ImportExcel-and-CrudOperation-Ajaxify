from django.contrib import admin
from .models import Number_store, CrudUser
from import_export.admin import ImportExportModelAdmin


# @admin.register(Number_store)
# class userdat(ImportExportModelAdmin):
#     pass

@admin.register(CrudUser)
class CrudAdmin(ImportExportModelAdmin):
    list_display = ('name', 'address','age')


# admin.site.register(CrudUser)
