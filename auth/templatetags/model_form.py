from django import template
from django.core.urlresolvers import reverse_lazy
from django.template.loader_tags import ConstantIncludeNode

register = template.Library()

def my_import(name): # from the python documentation, allows dots in import path
    components = name.split('.')
    mod = __import__(components[0])
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod

class ModelFormNode(template.Node):
    def __init__(self, parser, token, cls, template, url):
        self.parser = parser
        self.token = token
        self.cls = my_import(cls)
        self.template = template
        self.url = url

    def render(self, context):
        context.dicts[1].update(
            form=self.cls(),
            base="common/contents.html",
            action=reverse_lazy(self.url)
        )
        return ConstantIncludeNode(self.template).render(context)

def do_model_form(parser, token):
    bits = token.contents.split()
    return ModelFormNode(parser, token, *bits[1:])

register.tag('model_form', do_model_form)
