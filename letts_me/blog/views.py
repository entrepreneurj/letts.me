from django.shortcuts import render

from django.views.generic import ListView, DetailView

from blog.models import Entry

class BlogListView(ListView):
    model = Entry
    paginate_by = 5
    
    # Only shows published posts
    def get_queryset(self):
        return Entry.published.all()

class BlogDetailView(DetailView):
    model = Entry
