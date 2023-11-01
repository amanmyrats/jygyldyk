from django.urls import path

from .views import ReviewListView, ReviewUpdateView, ReviewDeleteView


list_view = ReviewListView
update_view = ReviewUpdateView
delete_view = ReviewDeleteView

urlpatterns = [
    path('', list_view.as_view(), name='reviews-list'),
    path('<int:pk>/', update_view.as_view(), name='reviews-update'),
    path('<int:pk>/delete/', delete_view.as_view(), name='reviews-delete'),
]