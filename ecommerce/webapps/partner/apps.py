from django.utils.translation import gettext_lazy as _

from core.application import OscarConfig


class PartnerConfig(OscarConfig):
    label = 'partner'
    name = 'webapps.partner'
    verbose_name = _('Partner')

    def ready(self):
        from . import receivers  # noqa
