from django.contrib import admin
from startapp.models import Institucion

class InstitucionAdmin(admin.ModelAdmin):
    list_display = ['institucion']

admin.site.register(Institucion, InstitucionAdmin)