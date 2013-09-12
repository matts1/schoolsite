from django.conf.urls import patterns
from groups.views import *

urlpatterns = patterns('',
    (
        'create', CreateClassView.as_view(), {}, 'create_class'
    )
)
