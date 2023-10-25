from api.utils.loading import get_api_class
from core.loading import get_model
from rest_framework import generics

from api.permissions import APIAdminPermission
from api.serializers.admin.partner import AdminStockRecordSerializer
from api.serializers.product import PartnerSerializer
from webapps.partner.models import StockRecord, Partner

# APIAdminPermission = get_api_class("permissions", "APIAdminPermission")
# AdminStockRecordSerializer = get_api_class(
#     "serializers.admin.partner", "AdminStockRecordSerializer"
# )
# PartnerSerializer = get_api_class("serializers.product", "PartnerSerializer")
# StockRecord = get_model("partner", "StockRecord")
# Partner = get_model("partner", "Partner")


class StockRecordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StockRecord.objects.all()
    serializer_class = AdminStockRecordSerializer
    permission_classes = (APIAdminPermission,)


class PartnerList(generics.ListCreateAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    permission_classes = (APIAdminPermission,)


class PartnerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    permission_classes = (APIAdminPermission,)
