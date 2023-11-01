from django.urls import path

from .views import (
    WeightBasedListView, WeightBasedCreateView, WeightBasedUpdateView, 
    WeightBasedDeleteView, WeightBasedDetailView, WeightBandUpdateView, 
    WeightBandDeleteView
)


weight_method_list_view = WeightBasedListView
weight_method_create_view = WeightBasedCreateView
weight_method_edit_view = WeightBasedUpdateView
weight_method_delete_view = WeightBasedDeleteView
# This doubles as the weight_band create view
weight_method_detail_view = WeightBasedDetailView
weight_band_edit_view = WeightBandUpdateView
weight_band_delete_view = WeightBandDeleteView

urlpatterns = [
    path('weight-based/', weight_method_list_view.as_view(), name='shipping-method-list'),
    path(
        'weight-based/create/',
        weight_method_create_view.as_view(),
        name='shipping-method-create'),
    path(
        'weight-based/<int:pk>/',
        weight_method_detail_view.as_view(),
        name='shipping-method-detail'),
    path(
        'weight-based/<int:pk>/edit/',
        weight_method_edit_view.as_view(),
        name='shipping-method-edit'),
    path(
        'weight-based/<int:pk>/delete/',
        weight_method_delete_view.as_view(),
        name='shipping-method-delete'),
    path(
        'weight-based/<int:method_pk>/bands/<int:pk>/',
        weight_band_edit_view.as_view(),
        name='shipping-method-band-edit'),
    path(
        'weight-based/<int:method_pk>/bands/<int:pk>/delete/',
        weight_band_delete_view.as_view(),
        name='shipping-method-band-delete'),
]