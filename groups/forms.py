from django.forms import *
from common.fields import *
from groups.models import Group


class CreateGroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['name']

    def is_valid(self):
        valid = super(CreateGroupForm, self).is_valid()
        if valid:
            self.save()
        return valid

    def save(self):
        data = self.cleaned_data
        Group(
            name=data['name'],
        ).save()
