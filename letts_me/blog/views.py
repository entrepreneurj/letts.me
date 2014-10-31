from django.shortcuts import render

from django.views.generic import ListView, DetailView

from blog.models import Entry


class AllBlogListView(ListView):
    model = Entry
    paginate_by = 5
    
    # Only shows published posts
    def get_queryset(self):
        return Entry.published.all()



class BlogBlogListView(ListView):
    model = Entry
    paginate_by = 5
    
    # Only shows published posts
    def get_queryset(self):
        return Entry.published.filter(categories__ancestor__name="blog")


class ReviewBlogListView(ListView):
    model = Entry
    paginate_by = 5
    
    # Only shows published posts
    def get_queryset(self):
        return Entry.published.filter(categories__ancestor__name="review")


class SoftwareBlogListView(ListView):
    model = Entry
    paginate_by = 5

    def get_queryset(self):
        return Entry.published.filter(categories__ancestor__name="software")

class BlogDetailView(DetailView):
    model = Entry
