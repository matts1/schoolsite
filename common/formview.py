from django.contrib import messages
from django.views.generic.edit import FormView

class FormView(FormView):
    extra_args = True
    def get_form_kwargs(self):
        kwargs = super(FormView, self).get_form_kwargs()
        for key, val in self.kwargs.items():
            kwargs[key] = val

        if self.extra_args:
            kwargs['request'] = self.request
            kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        if hasattr(self, 'success_message'):
            messages.add_message(self.request, messages.SUCCESS, self.success_message)
        return super(FormView, self).form_valid(form)
