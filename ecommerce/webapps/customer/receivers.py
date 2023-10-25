from django.dispatch import receiver

from webapps.catalogue.signals import product_viewed
from core.loading import get_class

CustomerHistoryManager = get_class('customer.history', 'CustomerHistoryManager')


@receiver(product_viewed)
def receive_product_view(sender, product, user, request, response, **kwargs):
    """
    Receiver to handle viewing single product pages

    Requires the request and response objects due to dependence on cookies
    """
    return CustomerHistoryManager.update(product, request, response)
