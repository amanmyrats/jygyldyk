from decimal import Decimal as D
from decimal import InvalidOperation

from babel.numbers import format_currency
from django import template
from django.conf import settings
from django.utils.translation import get_language, to_locale

register = template.Library()


@register.filter(name='currency')
def currency(value, currency=None):
    """
    Format decimal value as currency
    """
    if currency is None:
        currency = settings.DEFAULT_CURRENCY
    # For testing purposes
    currency = settings.DEFAULT_CURRENCY

    try:
        value = D(value)
    except (TypeError, InvalidOperation):
        return ""
    # Using Babel's currency formatting
    # http://babel.pocoo.org/en/latest/api/numbers.html#babel.numbers.format_currency
    CURRENCY_FORMAT = getattr(settings, 'CURRENCY_FORMAT', None)

    kwargs = {
        'currency': currency,
        'locale': to_locale(get_language() or settings.LANGUAGE_CODE)
    }

    if isinstance(CURRENCY_FORMAT, dict):
        kwargs.update(CURRENCY_FORMAT.get(currency, {}))
    else:
        kwargs['format'] = CURRENCY_FORMAT
    # locale always tk
    kwargs['locale'] = settings.LANGUAGE_CODE
    return format_currency(value, **kwargs)
