from django.contrib import admin

from groups.forms import CreateGroupForm
from groups.models import Group

class GroupAdmin(admin.ModelAdmin):
    model = Group
    form = CreateGroupForm



admin.site.register(Group, GroupAdmin)
