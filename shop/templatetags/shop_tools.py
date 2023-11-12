from django import template
from shop.models import Setting, Category

register = template.Library()

persian_digits = {
    "0": "۰",
    "1": "۱",
    "2": "۲",
    "3": "۳",
    "4": "۴",
    "5": "۵",
    "6": "۶",
    "7": "۷",
    "8": "۸",
    "9": "۹",
}


@register.simple_tag
def get_setting(setting_name):
    s = Setting.objects.first()
    try:
        # if setting_name == "site_logo":
        #     return s.site_logo.url
        # elif setting_name == "site_title":
        #     return s.site_title
        return getattr(s, setting_name).url
    except:
        return getattr(s, setting_name)


@register.simple_tag
def get_categories():
    return Category.objects.filter(level=0).order_by('title')


@register.filter
def to_persian_number(value):
    value = "".join([persian_digits.get(c, c) for c in value])
    return value
