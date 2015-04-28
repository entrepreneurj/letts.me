from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy

from links.views import LinksIndexView
from blog.views import BlogBlogListView, AllBlogListView, SoftwareBlogListView, ReviewBlogListView, BlogDetailView
from frontpage.views import IndexView, GalleryDetailView
from projects.views import ProjectListView, ProjectDetailView
urlpatterns = patterns('',
    # Examples:
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'links/$', RedirectView.as_view(url=reverse_lazy('links-index', args=[1])) ),
    url(r'links/(?P<page>[0-9]+)/$', LinksIndexView.as_view(), name='links-index'),
    url(r'posts/$', RedirectView.as_view(url=reverse_lazy('all-index', args=[1])) ),
    url(r'posts/all/(?P<page>[0-9]+)/$', AllBlogListView.as_view(), name='all-index'),
    url(r'posts/blog/(?P<page>[0-9]+)/$', BlogBlogListView.as_view(), name='blog-index'),
    url(r'posts/post/(?P<slug>[a-zA-Z0-9-_]+)/$', BlogDetailView.as_view(), name='blog-entry'),
    url(r'software/$', RedirectView.as_view(url=reverse_lazy('software-index', args=[1])) ),
    url(r'posts/software/(?P<page>[0-9]+)/$', SoftwareBlogListView.as_view(), name='software-index'),
    url(r'reviews/$', RedirectView.as_view(url=reverse_lazy('review-index', args=[1])) ),
    url(r'posts/reviews/(?P<page>[0-9]+)/$', ReviewBlogListView.as_view(), name='reviews-index'),
    url(r'projects/$', RedirectView.as_view(url=reverse_lazy('project-index', args=[1])), name='projects' ),
    url(r'projects/(?P<page>[0-9]+)/$', ProjectListView.as_view(), name='project-index'),
    url(r'projects/(?P<slug>[a-zA-Z0-9-_]+)/$', ProjectDetailView.as_view(), name='project'),
    url(r'gallery/(?P<slug>[a-zA-Z0-9-_]+)/$', GalleryDetailView.as_view(), name='gallery'),
     #url(r'^$', 'letts_me.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    # Historic redirects
    url(r'blog/$', RedirectView.as_view(url=reverse_lazy('blog-index', args=[1])) ),
    url(r'blog/(?P<slug>[a-zA-Z0-9-_]+)/$', BlogDetailView.as_view(), name='blog-entry'),

) 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
