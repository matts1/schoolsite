from django.shortcuts import redirect

def anonymous_required(fn):
    def new_fn(request, *args, **kwargs):
        if not request.user.is_authenticated():
            return fn(request, *args, **kwargs)
        else:
            return redirect('/MAKE_HOME_URL_EDIT_COMMON/LOGIN_DECORATORS.PY', permanent=False)
            # TODO: When home url is made, use that
            # return redirect(reverse_lazy('home'), permanent=False)
    return new_fn
