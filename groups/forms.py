from django.core.validators import RegexValidator
from django.forms import *
from groups.models import Group

def unused_key(key):
    if Group.objects.filter(key=key) and key != '':
        raise ValidationError('Someone else is using that key')

class CreateGroupForm(ModelForm):
    class Meta:
        model = Group

    def __init__(self, *args, **kwargs):
        super(CreateGroupForm, self).__init__(*args, **kwargs)
        self.fields['key'].validators.append(unused_key)
        self.fields['key'].required = False

    def clean(self):
        data = self.cleaned_data
        if not self._errors.get('key') and not data['visible'] and not data.get('key'):
            self._errors['key'] = self.error_class(['When your group is invisible it needs to have a key so that people can join it'])
        return super(CreateGroupForm, self).clean()

    def save(self):
        if self.model is None:
            self.model = Group(name='', visible=True, key='')
        data = self.cleaned_data
        self.model.name=data['name']
        self.model.visible=data['visible']
        self.model.key=data.get('key')
        return self.model
