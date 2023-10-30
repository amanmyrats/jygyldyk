from django.conf import settings

from core.loading import get_model


def get_default_review_status():
    # ProductReview = get_model('reviews', 'ProductReview')
    from .models import ProductReview
    ProductReview = ProductReview

    if settings.MODERATE_REVIEWS:
        return ProductReview.FOR_MODERATION

    return ProductReview.APPROVED
