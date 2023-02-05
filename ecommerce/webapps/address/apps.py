from django.utils.translation import gettext_lazy as _

from core.application import OscarConfig


class AddressConfig(OscarConfig):
    label = 'address'
    name = 'webapps.address'
    verbose_name = _('Address')
