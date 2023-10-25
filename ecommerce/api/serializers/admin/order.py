# pylint: disable=W0632
from rest_framework import serializers

from api.utils.loading import get_api_classes

from api.serializers.checkout import OrderSerializer, OrderLineSerializer, OrderLineAttributeSerializer

# OrderSerializer, OrderLineSerializer, OrderLineAttributeSerializer = get_api_classes(
#     "serializers.checkout",
#     ["OrderSerializer", "OrderLineSerializer", "OrderLineAttributeSerializer"],
# )


class AdminOrderSerializer(OrderSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="admin-order-detail")
    lines = serializers.HyperlinkedIdentityField(view_name="admin-order-lines-list")


class AdminOrderLineAttributeSerializer(OrderLineAttributeSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="admin-order-lineattributes-detail"
    )


class AdminOrderLineSerializer(OrderLineSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="admin-order-lines-detail")
    attributes = AdminOrderLineAttributeSerializer(
        many=True, fields=("url", "option", "value"), required=False
    )
