from django import template


register = template.Library()


@register.filter()
def censor(value):
   bad_words = ['salt', 'sugar', 'war']

   if not isinstance(value, str):
      raise TypeError(f'Wrong type - {type(value)}')

   for word in value.split():
      if word.lower() in bad_words:
         value = value.replace(word, f'{word[0]}{"*" * len(word)[1:]}')
   return value