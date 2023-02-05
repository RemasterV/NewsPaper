
from django import template


register = template.Library()


@register.simple_tag()
def news_time(x):
   return x.strftime('%d %b %Y')