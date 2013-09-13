from django import template
from django.template import Library, Node, TemplateSyntaxError
import urllib, hashlib, httplib

register = Library()

SIZE = 64

def gravatar(context):
    email = context['user'].email
    gravatar_url = 'http://www.gravatar.com/avatar/' + hashlib.md5(email.lower()).hexdigest() + '?'
    gravatar_url += urllib.urlencode({'d':'identicon', 's':str(SIZE)})
    return '<img src="%s">' % gravatar_url


register.simple_tag(gravatar, takes_context=True)
