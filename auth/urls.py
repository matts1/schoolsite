from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    (
        # TODO: redirect if already logged in
        r'^login$', 'django.contrib.auth.views.login',
        dict(template_name='auth/login.html'),
        'login'
    ),
)
