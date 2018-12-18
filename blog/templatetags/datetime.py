from django import template
from datetime import datetime

register = template.Library()


@register.filter
def iso_format(dt):
    new_dt = datetime.strptime(dt, '%Y-%m-%d %H:%M:%S')
    return new_dt.strftime("%B %d, %Y")
