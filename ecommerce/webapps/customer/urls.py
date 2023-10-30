from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _
from django.views import generic

from .views import (
    AccountSummaryView, OrderHistoryView, OrderDetailView, 
    AnonymousOrderDetailView, OrderLineView, AddressListView, 
    AddressCreateView, AddressUpdateView, AddressDeleteView, 
    AddressChangeStatusView, EmailHistoryView, EmailDetailView, 
    AccountAuthView, LogoutView, AccountRegistrationView, 
    ProfileView, ProfileUpdateView, ProfileDeleteView, ChangePasswordView
)

from webapps.communication.notifications.views import (
    InboxView, ArchiveView, UpdateView, DetailView
)


summary_view = AccountSummaryView
order_history_view = OrderHistoryView
order_detail_view = OrderDetailView
anon_order_detail_view = AnonymousOrderDetailView
order_line_view = OrderLineView

address_list_view = AddressListView
address_create_view = AddressCreateView
address_update_view = AddressUpdateView
address_delete_view = AddressDeleteView
address_change_status_view = AddressChangeStatusView

email_list_view = EmailHistoryView
email_detail_view = EmailDetailView
login_view = AccountAuthView
logout_view = LogoutView
register_view = AccountRegistrationView
profile_view = ProfileView
profile_update_view = ProfileUpdateView
profile_delete_view = ProfileDeleteView
change_password_view = ChangePasswordView

notification_inbox_view = InboxView
notification_archive_view = ArchiveView
notification_update_view = UpdateView
notification_detail_view = DetailView

from .alerts.views import (
    ProductAlertListView, ProductAlertCreateView, 
    ProductAlertConfirmView, ProductAlertCancelView
)

alert_list_view = ProductAlertListView
alert_create_view = ProductAlertCreateView
alert_confirm_view = ProductAlertConfirmView
alert_cancel_view = ProductAlertCancelView

from .wishlists.views import (
    WishListAddProduct, WishListListView, WishListDetailView, 
    WishListCreateView, WishListUpdateView, WishListDeleteView, 
    WishListRemoveProduct, WishListMoveProductToAnotherWishList
    )

wishlists_add_product_view = WishListAddProduct
wishlists_list_view = WishListListView
wishlists_detail_view = WishListDetailView
wishlists_create_view = WishListCreateView
wishlists_create_with_product_view = WishListCreateView
wishlists_update_view = WishListUpdateView
wishlists_delete_view = WishListDeleteView
wishlists_remove_product_view = WishListRemoveProduct
wishlists_move_product_to_another_view = WishListMoveProductToAnotherWishList

app_name = 'customer'

urlpatterns = [
    # Login, logout and register doesn't require login
            path('login/', login_view.as_view(), name='login'),
            path('logout/', logout_view.as_view(), name='logout'),
            path('register/', register_view.as_view(), name='register'),
            path('', login_required(summary_view.as_view()), name='summary'),
            path('change-password/', login_required(change_password_view.as_view()), name='change-password'),

            # Profile
            path('profile/', login_required(profile_view.as_view()), name='profile-view'),
            path('profile/edit/', login_required(profile_update_view.as_view()), name='profile-update'),
            path('profile/delete/', login_required(profile_delete_view.as_view()), name='profile-delete'),

            # Order history
            path('orders/', login_required(order_history_view.as_view()), name='order-list'),
            re_path(
                r'^order-status/(?P<order_number>[\w-]*)/(?P<hash>[A-z0-9-_=:]+)/$',
                anon_order_detail_view.as_view(), name='anon-order'
            ),
            path('orders/<str:order_number>/', login_required(order_detail_view.as_view()), name='order'),
            path(
                'orders/<str:order_number>/<int:line_id>/',
                login_required(order_line_view.as_view()),
                name='order-line'),

            # Address book
            path('addresses/', login_required(address_list_view.as_view()), name='address-list'),
            path('addresses/add/', login_required(address_create_view.as_view()), name='address-create'),
            path('addresses/<int:pk>/', login_required(address_update_view.as_view()), name='address-detail'),
            path(
                'addresses/<int:pk>/delete/',
                login_required(address_delete_view.as_view()),
                name='address-delete'),
            re_path(
                r'^addresses/(?P<pk>\d+)/(?P<action>default_for_(billing|shipping))/$',
                login_required(address_change_status_view.as_view()),
                name='address-change-status'),

            # Email history
            path('emails/', login_required(email_list_view.as_view()), name='email-list'),
            path('emails/<int:email_id>/', login_required(email_detail_view.as_view()), name='email-detail'),

            # Notifications
            # Redirect to notification inbox
            path(
                'notifications/', generic.RedirectView.as_view(url='/accounts/notifications/inbox/', permanent=False)),
            path(
                'notifications/inbox/',
                login_required(notification_inbox_view.as_view()),
                name='notifications-inbox'),
            path(
                'notifications/archive/',
                login_required(notification_archive_view.as_view()),
                name='notifications-archive'),
            path(
                'notifications/update/',
                login_required(notification_update_view.as_view()),
                name='notifications-update'),
            path(
                'notifications/<int:pk>/',
                login_required(notification_detail_view.as_view()),
                name='notifications-detail'),

            # Alerts
            # Alerts can be setup by anonymous users: some views do not
            # require login
            path('alerts/', login_required(alert_list_view.as_view()), name='alerts-list'),
            path('alerts/create/<int:pk>/', alert_create_view.as_view(), name='alert-create'),
            path('alerts/confirm/<str:key>/', alert_confirm_view.as_view(), name='alerts-confirm'),
            path('alerts/cancel/key/<str:key>/', alert_cancel_view.as_view(), name='alerts-cancel-by-key'),
            path(
                'alerts/cancel/<int:pk>/',
                login_required(alert_cancel_view.as_view()),
                name='alerts-cancel-by-pk'),

            # Wishlists
            path('wishlists/', login_required(wishlists_list_view.as_view()), name='wishlists-list'),
            path(
                'wishlists/add/<int:product_pk>/',
                login_required(wishlists_add_product_view.as_view()),
                name='wishlists-add-product'),
            path(
                'wishlists/<str:key>/add/<int:product_pk>/',
                login_required(wishlists_add_product_view.as_view()),
                name='wishlists-add-product'),
            path(
                'wishlists/create/',
                login_required(wishlists_create_view.as_view()),
                name='wishlists-create'),
            path(
                'wishlists/create/with-product/<int:product_pk>/',
                login_required(wishlists_create_view.as_view()),
                name='wishlists-create-with-product'),
            # Wishlists can be publicly shared, no login required
            path('wishlists/<str:key>/', wishlists_detail_view.as_view(), name='wishlists-detail'),
            path(
                'wishlists/<str:key>/update/',
                login_required(wishlists_update_view.as_view()),
                name='wishlists-update'),
            path(
                'wishlists/<str:key>/delete/',
                login_required(wishlists_delete_view.as_view()),
                name='wishlists-delete'),
            path(
                'wishlists/<str:key>/lines/<int:line_pk>/delete/',
                login_required(wishlists_remove_product_view.as_view()),
                name='wishlists-remove-product'),
            path(
                'wishlists/<str:key>/products/<int:product_pk>/delete/',
                login_required(wishlists_remove_product_view.as_view()),
                name='wishlists-remove-product'),
            path(
                'wishlists/<str:key>/lines/<int:line_pk>/move-to/<str:to_key>/',
                login_required(wishlists_move_product_to_another_view.as_view()),
                name='wishlists-move-product-to-another')
]