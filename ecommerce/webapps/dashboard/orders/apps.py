from django.urls import path
from django.utils.translation import gettext_lazy as _

from core.application import OscarDashboardConfig
from core.loading import get_class


class OrdersDashboardConfig(OscarDashboardConfig):
    label = 'orders_dashboard'
    name = 'webapps.dashboard.orders'
    verbose_name = _('Orders dashboard')

    default_permissions = ['is_staff', ]
    permissions_map = {
        'order-list': (['is_staff'], ['partner.dashboard_access']),
        'order-stats': (['is_staff'], ['partner.dashboard_access']),
        'order-detail': (['is_staff'], ['partner.dashboard_access']),
        'order-detail-note': (['is_staff'], ['partner.dashboard_access']),
        'order-line-detail': (['is_staff'], ['partner.dashboard_access']),
        'order-shipping-address': (['is_staff'], ['partner.dashboard_access']),
    }

    def ready(self):
        from .views import (
            OrderListView, OrderDetailView, ShippingAddressUpdateView, 
            LineDetailView, OrderStatsView
        )
        
        self.order_list_view = OrderListView
        self.order_detail_view = OrderDetailView
        self.shipping_address_view = ShippingAddressUpdateView
        self.line_detail_view = LineDetailView
        self.order_stats_view = OrderStatsView

    def get_urls(self):
        urls = [
            path('', self.order_list_view.as_view(), name='order-list'),
            path('statistics/', self.order_stats_view.as_view(), name='order-stats'),
            path('<str:number>/', self.order_detail_view.as_view(), name='order-detail'),
            path('<str:number>/notes/<int:note_id>/', self.order_detail_view.as_view(), name='order-detail-note'),
            path('<str:number>/lines/<int:line_id>/', self.line_detail_view.as_view(), name='order-line-detail'),
            path(
                '<str:number>/shipping-address/', self.shipping_address_view.as_view(), name='order-shipping-address'),
        ]
        return self.post_process_urls(urls)
