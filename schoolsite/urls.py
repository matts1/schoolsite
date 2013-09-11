from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

# discover the admin pages
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^auth/', include('auth.urls')),


    # page shortcuts
    url(r'^$', RedirectView.as_view(url=reverse_lazy('login'))),

    # admin and admin documentation
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
