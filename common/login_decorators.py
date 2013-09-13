from django.conf import settings
from django.shortcuts import redirect

def anonymous_required(fn):
    def new_fn(request, *args, **kwargs):
        if not request.user.is_authenticated():
            return fn(request, *args, **kwargs)
        else:
            return redirect(settings.LOGIN_REDIRECT_URL, permanent=False)
    return new_fn
