from django.core.validators import RegexValidator
from django.forms import *

class CharField(CharField):
    def __init__(self, *args, **kwargs):
        if hasattr(self, 'validators'):
            kwargs['validators'] = kwargs.get('validators', []) + self.validators
        if hasattr(self, 'max_length'):
            kwargs['max_length'] = kwargs.get('max_length', self.max_length)
        if hasattr(self, 'min_length'):
            kwargs['min_length'] = kwargs.get('min_length', self.min_length)
        super(CharField, self).__init__(*args, **kwargs)

class PasswordField(CharField):
    widget=PasswordInput()
    max_length=60

class NameField(CharField):
    max_length=40
    validators=[
        RegexValidator(regex=r'^[a-zA-Z]*$',
            message='Must be only letters',
            code='invalid_username'
        ),
    ]

    def to_python(self, value):
        return value.title()
