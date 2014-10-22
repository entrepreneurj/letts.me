from django.contrib import admin

from projects.models import Project

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("name",)}
admin.site.register(Project, ProjectAdmin)
