from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import (
    BasketView, BasketAddView, SavedView, VoucherAddView, VoucherRemoveView
)

summary_view = BasketView
saved_view = SavedView
add_view = BasketAddView
add_voucher_view = VoucherAddView
remove_voucher_view = VoucherRemoveView

urlpatterns = [
    path('', summary_view.as_view(), name='summary'),
    path('add/<int:pk>/', add_view.as_view(), name='add'),
    path('vouchers/add/', add_voucher_view.as_view(), name='vouchers-add'),
    path('vouchers/<int:pk>/remove/', remove_voucher_view.as_view(), name='vouchers-remove'),
    path('saved/', login_required(saved_view.as_view()), name='saved'),
]