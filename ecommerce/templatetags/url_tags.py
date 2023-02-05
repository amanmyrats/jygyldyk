from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def absolute_url(domain, path):
    return '{schema}://{domain}{path}'.format(
        schema=settings.URL_SCHEMA,
        domain=domain,
        path=path
    )
