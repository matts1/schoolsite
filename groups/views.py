from groups.forms import *
from django.views.generic import FormView, ListView

from groups.models import Group

class CreateGroupView(FormView):
    template_name = 'groups/create.html'
    form_class = CreateGroupForm

    def get_success_url(self):
        return '/abc' # TODO: make the success url the particular class page

class GroupListView(ListView):
    model = Group
