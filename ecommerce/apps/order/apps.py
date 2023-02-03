from django.utils.translation import gettext_lazy as _

from core.application import OscarConfig


class OrderConfig(OscarConfig):
    label = 'order'
    name = 'apps.order'
    verbose_name = _('Order')
