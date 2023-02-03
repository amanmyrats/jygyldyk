from django.utils.translation import gettext_lazy as _

from core.application import OscarConfig


class ShippingConfig(OscarConfig):
    label = 'shipping'
    name = 'apps.shipping'
    verbose_name = _('Shipping')
