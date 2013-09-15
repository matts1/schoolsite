from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import BaseCreateView
from django.views.generic.list import BaseListView
from groups.forms import *
from django.views.generic import FormView, ListView, UpdateView

from groups.models import Group

class GroupsView(FormView):
    template_name = 'groups/groups.html'
    form_class = CreateGroupForm

    def post(self, request, *args, **kwargs):
        # copied off django default, but modified to save the name of the group
        # so we can redirect to the right url
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            self.group = form.cleaned_data['name']
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('view_group', kwargs=dict(group=self.group))

    def get_context_data(self, **kwargs):
        kwargs['groups'] = Group.objects.all()
        return super(GroupsView, self).get_context_data(**kwargs)

class ViewGroupView(UpdateView):
    model = Group
    fields = ['visible', 'key']

    def get_success_url(self):
        return reverse_lazy('view_group', kwargs=dict(group=self.kwargs.get('group', '')))

    def get_object(self, queryset=None):
        return get_object_or_404(Group, name=self.kwargs.get('group', ''))
