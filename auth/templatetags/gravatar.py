from django.template import Library
import urllib, hashlib

register = Library()

SIZE = 64

def gravatar(context):
    email = context['user'].email
    gravatar_url = 'http://www.gravatar.com/avatar/' + hashlib.md5(email.lower()).hexdigest() + '?'
    gravatar_url += urllib.urlencode({'d':'identicon', 's':str(SIZE)})
    return (
        '<a class="gravatar" href="http://en.gravatar.com/">'
            '<img src="%s">'
            '<div class="image_overlay">Change Picture</div>'
        '</a>') % gravatar_url


register.simple_tag(gravatar, takes_context=True)
