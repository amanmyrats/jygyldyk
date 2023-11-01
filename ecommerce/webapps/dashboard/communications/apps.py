from django.urls import path
from django.utils.translation import gettext_lazy as _

from core.application import OscarDashboardConfig
from core.loading import get_class


class CommunicationsDashboardConfig(OscarDashboardConfig):
    label = 'communications_dashboard'
    name = 'webapps.dashboard.communications'
    verbose_name = _('Communications dashboard')

    default_permissions = ['is_staff', ]

    def ready(self):
        from .views import ListView, UpdateView
        
        self.list_view = ListView
        self.update_view = UpdateView

    def get_urls(self):
        urls = [
            path('', self.list_view.as_view(), name='comms-list'),
            path('<slug:slug>/', self.update_view.as_view(), name='comms-update'),
        ]
        return self.post_process_urls(urls)
