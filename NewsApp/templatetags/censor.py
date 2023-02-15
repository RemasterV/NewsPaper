#
from django import template

register = template.Library()


@register.simple_tag()
def censor(x):
   if isinstance(x, str):
      list_1 = ['редиска', 'морковь', 'репа']
      for i in list_1:
         while i in x.lower():
            print(len(x))
            y = x.lower().find(i)
            if y != -1:
               x = x[0:y + 1] + '*' * (len(i) - 1) + x[y + len(i):]
   return f'{x}'

