from django.contrib import admin

from projects.models import Project

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("name",)}
    class Media:
        js = [
        '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
        '/static/js/tinymce_setup.js',
    ]
admin.site.register(Project, ProjectAdmin)
