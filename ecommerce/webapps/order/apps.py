from django.utils.translation import gettext_lazy as _

from core.application import OscarConfig


class OrderConfig(OscarConfig):
    label = 'order'
    name = 'webapps.order'
    verbose_name = _('Order')
