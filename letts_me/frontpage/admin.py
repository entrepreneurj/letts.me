from django.contrib import admin

from frontpage.models import Category, Gallery, Image


class ImageInline(admin.TabularInline):
    model = Image
    extra = 4

class GalleryAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    prepopulated_fields = {"slug" : ("title",)}

admin.site.register(Category)

admin.site.register(Gallery, GalleryAdmin)
