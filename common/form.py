from django.forms import Form

class Form(Form):
    def __init__(self, request, user, *args, **kwargs):
        super(Form, self).__init__(*args, **kwargs)
        self.request = request
        self.user = user
