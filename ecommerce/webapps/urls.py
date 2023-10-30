from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy, include
from django.apps import apps
from django.conf import settings
from django.views.generic.base import RedirectView
from django.conf.urls.i18n import i18n_patterns

from core.application import OscarConfig
from core.loading import get_class
from views.decorators import login_forbidden



catalogue_app = apps.get_app_config('catalogue')
customer_app = apps.get_app_config('customer')
basket_app = apps.get_app_config('basket')
checkout_app = apps.get_app_config('checkout')
search_app = apps.get_app_config('search')
dashboard_app = apps.get_app_config('dashboard')
offer_app = apps.get_app_config('offer')
wishlists_app = apps.get_app_config('wishlists')


urlpatterns = [
    path('', RedirectView.as_view(url=settings.HOMEPAGE), name='home'),

    path('catalogue/', include('webapps.catalogue.urls')),
    path('basket/', include('webapps.basket.urls')),
    path('checkout/', include('webapps.checkout.urls')),
    path('accounts/', include('webapps.customer.urls')),
    path('search/', search_app.urls),
    path('dashboard/', dashboard_app.urls),
    path('offers/', offer_app.urls),
    path('wishlists/', wishlists_app.urls),
]