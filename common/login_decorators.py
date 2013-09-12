from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect

def anonymous_required(fn):
    def new_fn(request, *args, **kwargs):
        if not request.user.is_authenticated():
            return fn(request, *args, **kwargs)
        else:
            return redirect(reverse_lazy('home'), permanent=False)
    return new_fn
