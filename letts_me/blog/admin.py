from django.contrib import admin

from blog.models import Entry

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("title",)}



admin.site.register(Entry, BlogAdmin)
