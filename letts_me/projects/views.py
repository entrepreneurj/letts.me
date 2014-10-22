from django.shortcuts import render

from django.views.generic import ListView, DetailView

from projects.models import Project

class ProjectListView(ListView):
    model = Project
    paginate_by = 3
    

class ProjectDetailView(DetailView):
    model = Project
