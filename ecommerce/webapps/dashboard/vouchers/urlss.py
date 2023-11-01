from django.urls import path

from .views import (
    VoucherListView, VoucherCreateView, VoucherUpdateView, VoucherDeleteView, 
    VoucherStatsView, VoucherSetListView, VoucherSetCreateView, 
    VoucherSetUpdateView, VoucherSetDetailView, VoucherSetDownloadView, 
    VoucherSetDeleteView
)


list_view = VoucherListView
create_view = VoucherCreateView
update_view = VoucherUpdateView
delete_view = VoucherDeleteView
stats_view = VoucherStatsView

set_list_view = VoucherSetListView
set_create_view = VoucherSetCreateView
set_update_view = VoucherSetUpdateView
set_detail_view = VoucherSetDetailView
set_download_view = VoucherSetDownloadView
set_delete_view = VoucherSetDeleteView

urlpatterns = [
    path('', list_view.as_view(), name='voucher-list'),
    path('create/', create_view.as_view(), name='voucher-create'),
    path('update/<int:pk>/', update_view.as_view(), name='voucher-update'),
    path('delete/<int:pk>/', delete_view.as_view(), name='voucher-delete'),
    path('stats/<int:pk>/', stats_view.as_view(), name='voucher-stats'),

    path('sets/', set_list_view.as_view(), name='voucher-set-list'),
    path('sets/create/', set_create_view.as_view(), name='voucher-set-create'),
    path('sets/update/<int:pk>/', set_update_view.as_view(), name='voucher-set-update'),
    path('sets/detail/<int:pk>/', set_detail_view.as_view(), name='voucher-set-detail'),
    path('sets/download/<int:pk>/', set_download_view.as_view(), name='voucher-set-download'),
    path('sets/delete/<int:pk>/', set_delete_view.as_view(), name='voucher-set-delete'),
]