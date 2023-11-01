from django.urls import path

from .views import PageListView, PageCreateView, PageUpdateView, PageDeleteView


list_view = PageListView
create_view = PageCreateView
update_view = PageUpdateView
delete_view = PageDeleteView

urlpatterns = [
    path('', list_view.as_view(), name='page-list'),
    path('create/', create_view.as_view(), name='page-create'),
    path('update/<str:pk>/', update_view.as_view(), name='page-update'),
    path('delete/<str:pk>/', delete_view.as_view(), name='page-delete')
]