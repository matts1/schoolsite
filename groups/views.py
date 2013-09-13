from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from groups.forms import *
from django.views.generic import FormView, ListView

from groups.models import Group

class CreateGroupView(FormView):
    template_name = 'auth/register.html'
    form_class = CreateGroupForm

    def get_success_url(self):
        return '/abc' # TODO: make the success url the class page

class GroupListView(ListView):
    model = Group

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GroupListView, self).dispatch(*args, **kwargs)
