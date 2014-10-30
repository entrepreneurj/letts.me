from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy

from links.views import LinksIndexView
from blog.views import BlogListView, BlogDetailView
from frontpage.views import IndexView 
from projects.views import ProjectListView, ProjectDetailView
urlpatterns = patterns('',
    # Examples:
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'links/$', RedirectView.as_view(url=reverse_lazy('links-index', args=[1])) ),
    url(r'links/(?P<page>[0-9]+)/$', LinksIndexView.as_view(), name='links-index'),
    url(r'blog/$', RedirectView.as_view(url=reverse_lazy('blog-index', args=[1])) ),
    url(r'blog/(?P<page>[0-9]+)/$', BlogListView.as_view(), name='blog-index'),
    url(r'blog/(?P<slug>[a-zA-Z0-9-_]+)/$', BlogDetailView.as_view(), name='blog-entry'),
    url(r'projects/$', RedirectView.as_view(url=reverse_lazy('project-index', args=[1])), name='projects' ),
    url(r'projects/(?P<page>[0-9]+)/$', ProjectListView.as_view(), name='project-index'),
    url(r'projects/(?P<slug>[a-zA-Z0-9-_]+)/$', ProjectDetailView.as_view(), name='project'),
     #url(r'^$', 'letts_me.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

) 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
