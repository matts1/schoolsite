from django import template
from django.template import Library, Node, TemplateSyntaxError
import urllib, hashlib, httplib

register = Library()

GRAVATAR_DOMAIN = 'gravatar.com'
GRAVATAR_PATH = '/avatar/'
SIZE = 64
DEFAULT = 'http://www.artifacting.com/blog/wp-content/uploads/2010/11/Abe_Lincoln.jpg'

def gravatar(context):
    email = context['user'].email
    gravatar_url = 'http://www.gravatar.com/avatar/' + hashlib.md5(email.lower()).hexdigest() + '?'
    gravatar_url += urllib.urlencode({'d':DEFAULT, 's':str(SIZE)})
    return '<img src="%s">' % gravatar_url


register.simple_tag(gravatar, takes_context=True)
