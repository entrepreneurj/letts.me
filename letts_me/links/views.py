from django.shortcuts import render

from django.views.generic import TemplateView, ListView

from links.models import Link

class IndexView(TemplateView):

    template_name = "index.html"

class LinksIndexView(ListView):
    template_name = "link_index.html"
    model = Link

    paginate_by = 5
