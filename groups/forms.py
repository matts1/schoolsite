from django.forms import *
from common.fields import *

class CreateClassForm(Form):
    group_name = NameField()

