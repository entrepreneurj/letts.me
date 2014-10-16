from django.contrib import admin

from blog.models import Entry
from links.models import Link

class LinksInline(admin.TabularInline):
    model = Link
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("title",)}
    inlines = [LinksInline]
    
    class Media:
        js = [
        '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
        '/static/js/tinymce_setup.js',
	]    	

admin.site.register(Entry, BlogAdmin)
