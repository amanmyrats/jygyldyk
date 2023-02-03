from django.utils.translation import gettext_lazy as _

from core.application import OscarConfig


class PaymentConfig(OscarConfig):
    label = 'payment'
    name = 'apps.payment'
    verbose_name = _('Payment')
