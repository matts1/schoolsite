from django.contrib.auth.views import login
from django.core.urlresolvers import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import FormView

from auth.forms import *
from common.login_decorators import anonymous_required

# using a function here rather than class because django uses a function, unfortunately
@anonymous_required
def custom_login(*args, **kwargs):
    return login(*args, **kwargs)

class RegisterView(FormView):
    template_name = 'auth/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    success_message = 'Your account has been created. You may now log in'

    @method_decorator(anonymous_required)
    def get(self, *args, **kwargs):
        return super(RegisterView, self).get(*args, **kwargs)
