from django.utils.translation import gettext_lazy as _

from core.application import OscarConfig


class CommunicationConfig(OscarConfig):
    label = 'communication'
    name = 'apps.communication'
    verbose_name = _('Communication')
