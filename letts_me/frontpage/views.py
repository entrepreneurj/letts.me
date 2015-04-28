from django.shortcuts import render

from django.views.generic import TemplateView, DetailView

from links.models import Link
from blog.models import Entry

from .models import Gallery 
class IndexView(TemplateView):

    template_name = "frontpage/index.html"

    def get_context_data(self, **kwargs):

        context = super(IndexView, self).get_context_data(**kwargs)
        context["blog_post"] = Entry.published.filter(categories__ancestor__name="blog")[0]
        context["software_post"] = Entry.published.filter(categories__ancestor__name="software")[0]
        context["link"] = Link.link_manager.latest()
        return context

class GalleryDetailView(DetailView):
   
   model = Gallery
