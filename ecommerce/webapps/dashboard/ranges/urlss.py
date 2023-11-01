from django.urls import path

from .views import (
    RangeListView, RangeCreateView, RangeUpdateView, 
    RangeDeleteView, RangeProductListView, RangeReorderView
)


list_view = RangeListView
create_view = RangeCreateView
update_view = RangeUpdateView
delete_view = RangeDeleteView
products_view = RangeProductListView
reorder_view = RangeReorderView

urlpatterns = [
    path('', list_view.as_view(), name='range-list'),
    path('create/', create_view.as_view(), name='range-create'),
    path('<int:pk>/', update_view.as_view(), name='range-update'),
    path('<int:pk>/delete/', delete_view.as_view(), name='range-delete'),
    path('<int:pk>/products/', products_view.as_view(), name='range-products'),
    path('<int:pk>/reorder/', reorder_view.as_view(), name='range-reorder'),
]