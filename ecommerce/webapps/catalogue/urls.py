"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path

from core.loading import get_class


detail_view = get_class('catalogue.views', 'ProductDetailView')
catalogue_view = get_class('catalogue.views', 'CatalogueView')
category_view = get_class('catalogue.views', 'ProductCategoryView')
range_view = get_class('offer.views', 'RangeDetailView')


urlpatterns = [
    path('', catalogue_view.as_view(), name='index'),
    re_path(
        r'^(?P<product_slug>[\w-]*)_(?P<pk>\d+)/$',
        detail_view.as_view(), name='detail'),
    re_path(
        r'^category/(?P<category_slug>[\w-]+(/[\w-]+)*)_(?P<pk>\d+)/$',
        category_view.as_view(), name='category'),
    path('ranges/<slug:slug>/', range_view.as_view(), name='range'),
]
