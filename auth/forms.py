from copy import deepcopy
from django.contrib.auth.forms import AuthenticationForm
from django.forms import *

from auth.models import User
from common.fields import *

def unused_email(email):
    if User.objects.filter(email=email):
        raise ValidationError('The email is already taken')

class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['email'].validators.append(unused_email)
        self.fields['password'].widget = PasswordInput()
        # deepcopy so we can change the label
        self.fields['confirm_password'] = deepcopy(self.fields['password'])
        self.fields['confirm_password'].label = 'Confirm Password'

    def clean(self):
        data = self.cleaned_data
        same = data.get('password', '') == data.get('confirm_password', '')
        if not same:
            self._errors['confirm_password'] = self.error_class(['Passwords Must Match'])
        return super(RegisterForm, self).clean()

    def is_valid(self):
        valid = super(RegisterForm, self).is_valid()
        if valid:
            self.save()
        return valid

    def save(self):
        data = self.cleaned_data
        user = User.objects.create_user(
            data['email'], # use email as username since it's required
            data['email'],
            data['password'],
            first_name=data['first_name'].title(),
            last_name=data['last_name'].title(),
        )
        user.save()

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Email Address'
