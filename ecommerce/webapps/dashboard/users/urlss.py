from django.urls import path, re_path

from .views import (
    IndexView, UserDetailView, PasswordResetView, ProductAlertListView, 
    ProductAlertUpdateView, ProductAlertDeleteView
)


index_view = IndexView
user_detail_view = UserDetailView
password_reset_view = PasswordResetView
alert_list_view = ProductAlertListView
alert_update_view = ProductAlertUpdateView
alert_delete_view = ProductAlertDeleteView

urlpatterns = [
    path('', index_view.as_view(), name='users-index'),
    re_path(r'^(?P<pk>-?\d+)/$', user_detail_view.as_view(), name='user-detail'),
    re_path(
        r'^(?P<pk>-?\d+)/password-reset/$',
        password_reset_view.as_view(),
        name='user-password-reset'),

    # Alerts
    path('alerts/', alert_list_view.as_view(), name='user-alert-list'),
    re_path(r'^alerts/(?P<pk>-?\d+)/delete/$', alert_delete_view.as_view(), name='user-alert-delete'),
    re_path(r'^alerts/(?P<pk>-?\d+)/update/$', alert_update_view.as_view(), name='user-alert-update'),
]