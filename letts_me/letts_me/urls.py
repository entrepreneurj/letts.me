from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from links.views import LinksIndexView
urlpatterns = patterns('',
    # Examples:
     url(r'^$', LinksIndexView.as_view(), name='home'),
     #url(r'^$', 'letts_me.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
