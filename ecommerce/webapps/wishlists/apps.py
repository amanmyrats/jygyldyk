from django.urls import path
from django.utils.translation import gettext_lazy as _

from core.application import OscarConfig
from core.loading import get_class


class WishlistsConfig(OscarConfig):
    label = 'wishlists'
    name = 'webapps.wishlists'
    verbose_name = _('Wishlists')

    namespace = 'wishlists'

    def ready(self):
        self.wishlist_view = get_class('wishlists.views', 'WishListView')

    def get_urls(self):
        urls = [
            path('<str:key>/', self.wishlist_view.as_view(), name='detail'),
        ]

        return self.post_process_urls(urls)
