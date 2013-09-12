from groups.forms import *
from django.views.generic import FormView

class CreateClassView(FormView):
    template_name = 'auth/register.html'
    form_class = CreateClassForm

    def get_success_url(self):
        return '/abc' # TODO: make the success url the class page
