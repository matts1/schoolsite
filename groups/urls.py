from django.conf.urls import patterns

from groups.views import *

urlpatterns = patterns('',
    (
        r'^create$', CreateGroupView.as_view(), {}, 'create_class',
    ),
    (
        r'^home$', GroupListView.as_view(), {}, 'home',
    ),
)
