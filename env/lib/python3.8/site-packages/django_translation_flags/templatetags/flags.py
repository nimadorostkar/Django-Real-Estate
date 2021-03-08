from django import template

register = template.Library()


@register.inclusion_tag('languages.html', takes_context=True)
def languages(context, flag_type='', **kwargs):
    """
    Templatetag languages

    :param context: Getting context
    :param flag_type: Default empty, It acepts the string 'square'
    :param kwargs: Classes to HTML tags
    :return: A dict with classes
    """
    if flag_type == 'square':
        flag_type = 'flag-icon-square'
    default = dict(li_class='', a_class='')
    classes = dict(default, **kwargs)
    return {
        'icon_class': flag_type,
        'classes': classes,
        'redirect_to': context.request.get_full_path
    }
