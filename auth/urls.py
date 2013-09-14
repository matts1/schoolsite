from django.conf.urls import patterns
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.views import login

from auth.views import *
from auth.forms import LoginForm
from common.login_decorators import anonymous_required

urlpatterns = patterns('',
    (
        r'^login$', anonymous_required(login),
        dict(template_name='auth/login.html', authentication_form=LoginForm),
        'login'
    ),
    (
        r'^logout$', 'django.contrib.auth.views.logout',
        dict(next_page=reverse_lazy('login')),
        'logout'
    ),
    (
        r'^register$', anonymous_required(RegisterView.as_view()), {}, 'register'
    ),
)
