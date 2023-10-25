# pylint: disable=W0632

import functools

from core.loading import get_class, get_model

from rest_framework import generics

from api import permissions
from api.basket.operations import (
    assign_basket_strategy,
    editable_baskets,
    get_anonymous_basket,
    prepare_basket,
)
from api.utils.loading import get_api_classes, get_api_class

from .utils import QuerySetList

from webapps.basket.models import Basket, LineAttribute
from webapps.catalogue.models import (
    Product, Option
)
from webapps.address.models import Country
from webapps.offer.models import Range


__all__ = (
    "BasketList",
    "BasketDetail",
    "LineAttributeDetail",
    "OptionList",
    "OptionDetail",
    "CountryList",
    "CountryDetail",
)

# Basket = get_model("basket", "Basket")
# LineAttribute = get_model("basket", "LineAttribute")
# Product = get_model("catalogue", "Product")
# Option = get_model("catalogue", "Option")
# Country = get_model("address", "Country")
# Range = get_model("offer", "Range")

from webapps.partner.strategy import Selector
from api.serializers.checkout import CountrySerializer
from api.serializers.basket import BasketSerializer, LineAttributeSerializer

# Selector = get_class("partner.strategy", "Selector")
# CountrySerializer = get_api_class("serializers.checkout", "CountrySerializer")
# (
#     BasketSerializer,
#     LineAttributeSerializer,
# ) = get_api_classes(  # pylint: disable=unbalanced-tuple-unpacking
#     "serializers.basket", ["BasketSerializer", "LineAttributeSerializer"]
# )

from api.serializers.product import RangeSerializer, OptionSerializer
# (
#     RangeSerializer,
#     OptionSerializer,
# ) = get_api_classes(  # pylint: disable=unbalanced-tuple-unpacking
#     "serializers.product", ["RangeSerializer", "OptionSerializer"]
# )


class CountryList(generics.ListAPIView):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()


class CountryDetail(generics.RetrieveAPIView):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()


class BasketList(generics.ListAPIView):
    """
    Retrieve all baskets that belong to the current (authenticated) user.
    """

    serializer_class = BasketSerializer
    queryset = editable_baskets()

    def get_queryset(self):
        qs = super(BasketList, self).get_queryset()

        if self.request.user.is_authenticated:
            qs = qs.filter(owner=self.request.user)
            mapped_with_baskets = list(
                map(functools.partial(assign_basket_strategy, request=self.request), qs)
            )
        else:  # anonymous users have max 1 basket.
            basket = get_anonymous_basket(self.request)
            mapped_with_baskets = [prepare_basket(basket, self.request)]

        return QuerySetList(mapped_with_baskets, qs)


class BasketDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BasketSerializer
    permission_classes = (permissions.RequestAllowsAccessTo,)
    queryset = editable_baskets()

    def get_object(self):
        basket = super(BasketDetail, self).get_object()
        return assign_basket_strategy(basket, self.request)


class LineAttributeDetail(generics.RetrieveUpdateAPIView):
    queryset = LineAttribute.objects.all()
    serializer_class = LineAttributeSerializer
    permission_classes = (permissions.RequestAllowsAccessTo,)


class OptionList(generics.ListAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer


class OptionDetail(generics.RetrieveAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer


class RangeList(generics.ListAPIView):
    queryset = Range.objects.all()
    serializer_class = RangeSerializer


class RangeDetail(generics.RetrieveAPIView):
    queryset = Range.objects.all()
    serializer_class = RangeSerializer
