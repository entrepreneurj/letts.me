from django.contrib import admin

from blog.models import Entry
from links.models import Link
from frontpage.models import Gallery

class LinksInline(admin.TabularInline):
    model = Link
    extra = 1

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("title",)}
    inlines = [LinksInline]
    
    class Media:
        js = [
        '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
        '/static/js/tinymce_setup.js',
	]    	

admin.site.register(Entry, BlogAdmin)
