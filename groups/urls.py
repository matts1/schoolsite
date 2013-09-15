from django.conf.urls import patterns
from django.contrib.auth.decorators import login_required

from groups.views import *

urlpatterns = patterns('',
    (
        r'^home$', login_required(GroupsView.as_view()), {}, 'home',
    ),
    (
        r'^viewclass/(?P<group>[A-Za-z0-9 ]+)$',
        login_required(ViewGroupView.as_view()), {}, 'view_group',
    ),
)
