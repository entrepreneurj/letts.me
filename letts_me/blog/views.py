from django.shortcuts import render

from django.views.generic import ListView, DetailView

from blog.models import Entry

class BlogListView(ListView):
    model = Entry
    paginate_by = 5

class BlogDetailView(DetailView):
    model = Entry
