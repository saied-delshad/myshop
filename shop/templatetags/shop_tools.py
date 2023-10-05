from django import template
from shop.models import Setting, Category

register = template.Library()


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

