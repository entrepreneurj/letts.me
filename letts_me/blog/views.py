from django.shortcuts import render

from django.views.generic import ListView, DetailView

from blog.models import Entry


class AllBlogListView(ListView):
    model = Entry
    paginate_by = 5
    
    # Only shows published posts
    def get_queryset(self):
        return Entry.published.all()
    
    def get_context_data(self, **kwargs):
        context=super(AllBlogListView, self).get_context_data(**kwargs)
        context["blog_page_title"]="All Posts"
        return context


class BlogBlogListView(ListView):
    model = Entry
    paginate_by = 5
    
    # Only shows published posts
    def get_queryset(self):
        return Entry.published.filter(categories__ancestor__name="blog")
    
    def get_context_data(self, **kwargs):
        context=super(BlogBlogListView, self).get_context_data(**kwargs)
        context["blog_page_title"]="Blog Posts"
        return context


class ReviewBlogListView(ListView):
    model = Entry
    paginate_by = 5
    
    # Only shows published posts
    def get_queryset(self):
        return Entry.published.filter(categories__ancestor__name="review")
    
    def get_context_data(self, **kwargs):
        context=super(ReviewBlogListView, self).get_context_data(**kwargs)
        context["blog_page_title"]="Reviews"
        return context


class SoftwareBlogListView(ListView):
    model = Entry
    paginate_by = 5

    def get_queryset(self):
        return Entry.published.filter(categories__ancestor__name="software")
    
    def get_context_data(self, **kwargs):
        context=super(SoftwareBlogListView, self).get_context_data(**kwargs)
        context["blog_page_title"]="Software Posts"
        return context

class BlogDetailView(DetailView):
    model = Entry
