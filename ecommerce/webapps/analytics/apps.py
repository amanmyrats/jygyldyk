from django.utils.translation import gettext_lazy as _

from core.application import OscarConfig


class AnalyticsConfig(OscarConfig):
    label = 'analytics'
    name = 'webapps.analytics'
    verbose_name = _('Analytics')

    def ready(self):
        from . import receivers  # noqa
