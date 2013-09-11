from django.forms import *
from django.core.validators import *
from django.contrib.auth.models import User
from auth.models import UserProfile

from common.form import Form

def is_valid_username(username):
    if User.objects.filter(username=username):
        raise ValidationError('The username is already taken')

def is_valid_email(email):
    if User.objects.filter(email=email):
        raise ValidationError('The email is already taken')

def password_field():
    return CharField(
        widget=PasswordInput(),
        max_length=60,
    )

class RegisterForm(Form):
    user = CharField(
        max_length=30,
        validators=[
            RegexValidator(regex=r'^[a-z0-9_]*$',
                message='Username must be Alphanumeric and Lowercase',
                code='invalid_username'
            ),
            is_valid_username
        ]
    )
    email = EmailField(max_length=30, validators=[is_valid_email])
    password = password_field()
    confirm_password = password_field()

    def clean(self):
        data = self.cleaned_data
        same = data.get('password', '') == data.get('confirm_password', '')
        if not same:
            for field in ['password', 'confirm_password']:
                self._errors[field] = self.error_class(['Passwords Must Match'])
        return super(RegisterForm, self).clean()

    def save(self):
        data = self.cleaned_data
        user = User.objects.create_user(
            data['user'],
            data['email'],
            data['password']
        )
        user.save()
        profile = UserProfile(
            user=user,

        )
        profile.save()
