from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import (
    ProductReviewDetail, CreateProductReview, AddVoteView, ProductReviewList
)

detail_view = ProductReviewDetail
create_view = CreateProductReview
vote_view = AddVoteView
list_view = ProductReviewList

urlpatterns = [
    path('<int:pk>/', detail_view.as_view(), name='reviews-detail'),
    path('add/', create_view.as_view(), name='reviews-add'),
    path('<int:pk>)/vote/', login_required(vote_view.as_view()), name='reviews-vote'),
    path('', list_view.as_view(), name='reviews-list'),
]