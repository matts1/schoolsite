from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView

from auth.forms import *

class RegisterView(FormView):
    template_name = 'auth/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    success_message = 'Your account has been created. You may now log in'
