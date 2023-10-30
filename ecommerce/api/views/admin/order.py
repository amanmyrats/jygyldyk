# pylint: disable=unbalanced-tuple-unpacking
from rest_framework import generics

from core.loading import get_model
from api.utils.loading import get_api_classes, get_api_class
from api.permissions import APIAdminPermission
from api.serializers.admin.order import AdminOrderSerializer, AdminOrderLineSerializer, AdminOrderLineAttributeSerializer

from webapps.order.models import Order, Line, LineAttribute


# APIAdminPermission = get_api_class("permissions", "APIAdminPermission")
# Order = get_model("order", "Order")
# OrderLine = get_model("order", "Line")
# OrderLineAttribute = get_model("order", "LineAttribute")
OrderLine = Line
OrderLineAttribute = LineAttribute

# (
#     AdminOrderSerializer,
#     AdminOrderLineSerializer,
#     AdminOrderLineAttributeSerializer,
# ) = get_api_classes(  # noqa
#     "serializers.admin.order",
#     [
#         "AdminOrderSerializer",
#         "AdminOrderLineSerializer",
#         "AdminOrderLineAttributeSerializer",
#     ],
# )


class OrderAdminList(generics.ListAPIView):
    serializer_class = AdminOrderSerializer
    queryset = Order.objects.get_queryset()
    permission_classes = (APIAdminPermission,)


class OrderAdminDetail(generics.RetrieveDestroyAPIView):
    serializer_class = AdminOrderSerializer
    queryset = Order.objects.get_queryset()
    permission_classes = (APIAdminPermission,)


class OrderLineAdminList(generics.ListAPIView):
    serializer_class = AdminOrderLineSerializer
    queryset = OrderLine.objects.get_queryset()
    permission_classes = (APIAdminPermission,)

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        return super().get_queryset().filter(order_id=pk)


class OrderLineAdminDetail(generics.RetrieveDestroyAPIView):
    serializer_class = AdminOrderLineSerializer
    queryset = OrderLine.objects.get_queryset()
    permission_classes = (APIAdminPermission,)


class OrderLineAttributeAdminDetail(generics.RetrieveDestroyAPIView):
    serializer_class = AdminOrderLineAttributeSerializer
    queryset = OrderLineAttribute.objects.get_queryset()
    permission_classes = (APIAdminPermission,)