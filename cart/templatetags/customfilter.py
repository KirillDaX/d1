from django.template.defaultfilters import register, stringfilter


@register.filter(is_safe=False)
@stringfilter
def pluralize(value, forms):
    """
    Ставим правильное окончание после числа
    {{item_count|pluralize:"товар,товара,товаров"}}
    """
    try:
        one, two, many = forms.split(u',')
        value = str(value)[-2:]

        if 21 > int(value) > 4:
            return many

        if value.endswith('1'):
            return one
        elif value.endswith(('2', '3', '4')):
            return two
        else:
            return many

    except (ValueError, TypeError):
        return ''
