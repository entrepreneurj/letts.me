from django.shortcuts import render

from django.views.generic import TemplateView



class LinksIndexView(TemplateView):

    template_name = "index.html"
