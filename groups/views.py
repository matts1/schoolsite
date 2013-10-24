from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from groups.forms import *
from django.views.generic import FormView, UpdateView

from groups.models import Group

def post(self, request, *args, **kwargs):
    # copied off django default, but modified to save the name of the group
    # so we can redirect to the right url
    self.object = self.get_object()
    form_class = self.get_form_class()
    form = self.get_form(form_class)
    form.model = self.object
    if form.is_valid():
        self.group = form.cleaned_data.get('name')
        return self.form_valid(form)
    else:
        return self.form_invalid(form)

class GroupsView(FormView):
    template_name = 'groups/groups.html'
    form_class = CreateGroupForm

    def post(self, request, *args, **kwargs):
        # copied off django default, but modified to save the name of the group
        # so we can redirect to the right url
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        self.object = self.get_object()
        form.model = self.object
        if form.is_valid():
            self.group = form.cleaned_data.get('name')
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('view_group', kwargs=dict(group=self.group))

    def get_context_data(self, **kwargs):
        kwargs['groups'] = Group.objects.all()
        return super(GroupsView, self).get_context_data(**kwargs)

    def get_object(self, queryset=None):
        return None

    def form_valid(self, form):
        self.object = form.save()
        self.object.save()
        return super(GroupsView, self).form_valid(form)

class ViewGroupView(UpdateView):
    model = Group
    form_class = CreateGroupForm

    post = post

    def get_success_url(self):
        return reverse_lazy('view_group', kwargs=dict(group=self.kwargs.get('group', '')))

    def get_object(self, queryset=None):
        return get_object_or_404(Group, name=self.kwargs.get('group', ''))

    def form_valid(self, form):
        self.object = form.save(self.object)
        self.object.save()
        return super(ViewGroupView, self).form_valid(form)
