from django.forms import *
from common.fields import *

class CreateGroupForm(Form):
    group_name = NameField()

