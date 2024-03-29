from django.urls import path
from django.utils.translation import gettext_lazy as _

from core.application import OscarDashboardConfig
from core.loading import get_class


class ReportsDashboardConfig(OscarDashboardConfig):
    label = 'reports_dashboard'
    name = 'webapps.dashboard.reports'
    verbose_name = _('Reports dashboard')

    default_permissions = ['is_staff', ]

    def ready(self):
        from webapps.dashboard.reports.views import IndexView
        # self.index_view = get_class('dashboard.reports.views', 'IndexView')
        self.index_view = IndexView

    def get_urls(self):
        urls = [
            path('', self.index_view.as_view(), name='reports-index'),
        ]
        return self.post_process_urls(urls)
