
from django.contrib import admin

# Register your models here.
from .models import *


class FilesAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_exel_file', 'second_exel_file', 'out_file')
    list_display_links = ('id',)


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'images',)
    list_display_links = ('id',)


admin.site.register(Uploader,FilesAdmin)
admin.site.register(Photo,PhotoAdmin)
