from django.urls import path

from .views import IndexView


index_view = IndexView

urlpatterns = [
    path('', index_view.as_view(), name='reports-index'),
]