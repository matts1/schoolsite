from django.conf.urls import patterns
from django.core.urlresolvers import reverse_lazy

from auth.views import *
from auth.forms import LoginForm

urlpatterns = patterns('',
    (
        r'^login$', custom_login,
        dict(template_name='auth/login.html', authentication_form=LoginForm),
        'login'
    ),
    (
        r'^logout$', 'django.contrib.auth.views.logout',
        dict(next_page=reverse_lazy('login')),
        'logout'
    ),
    (
        r'^register$', RegisterView.as_view(), {}, 'register'
    ),
)
