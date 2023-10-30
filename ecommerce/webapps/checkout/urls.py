from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import (
    IndexView, ShippingAddressView, UserAddressUpdateView, UserAddressDeleteView, 
    ShippingMethodView, PaymentMethodView, PaymentDetailsView ,ThankYouView
)

index_view = IndexView
shipping_address_view = ShippingAddressView
user_address_update_view = UserAddressUpdateView
user_address_delete_view = UserAddressDeleteView
shipping_method_view = ShippingMethodView
payment_method_view = PaymentMethodView
payment_details_view = PaymentDetailsView
thankyou_view = ThankYouView

app_name='checkout'

urlpatterns = [
    path('', index_view.as_view(), name='index'),

    # Shipping/user address views
    path('shipping-address/', shipping_address_view.as_view(), name='shipping-address'),
    path('user-address/edit/<int:pk>/', login_required(user_address_update_view.as_view()), name='user-address-update'),
    path('user-address/delete/<int:pk>/', login_required(user_address_delete_view.as_view()), name='user-address-delete'),

    # Shipping method views
    path('shipping-method/', shipping_method_view.as_view(), name='shipping-method'),

    # Payment views
    path('payment-method/', payment_method_view.as_view(), name='payment-method'),
    path('payment-details/', payment_details_view.as_view(), name='payment-details'),

    # Preview and thankyou
    path('preview/', payment_details_view.as_view(preview=True), name='preview'),
    path('thank-you/', thankyou_view.as_view(), name='thank-you'),
]