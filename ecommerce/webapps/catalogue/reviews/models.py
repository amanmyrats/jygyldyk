from webapps.catalogue.reviews.abstract_models import (
    AbstractProductReview, AbstractVote)
from core.loading import is_model_registered

if not is_model_registered('reviews', 'ProductReview'):
    class ProductReview(AbstractProductReview):
        pass


if not is_model_registered('reviews', 'Vote'):
    class Vote(AbstractVote):
        pass
