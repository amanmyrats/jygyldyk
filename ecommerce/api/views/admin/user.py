from django.contrib.auth import get_user_model
from api.utils.loading import get_api_class
from rest_framework import generics

from api.permissions import APIAdminPermission
from api.serializers.admin.user import AdminUserSerializer

# APIAdminPermission = get_api_class("permissions", "APIAdminPermission")
# AdminUserSerializer = get_api_class("serializers.admin.user", "AdminUserSerializer")
User = get_user_model()


class UserAdminList(generics.ListCreateAPIView):
    """
    List of all users, either frontend or admin users.
    The fields shown in this view can be changed using the ``OSCARAPI_ADMIN_USER_FIELDS``
    setting
    """

    queryset = User.objects.all()
    serializer_class = AdminUserSerializer
    permission_classes = (APIAdminPermission,)


class UserAdminDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = AdminUserSerializer
    permission_classes = (APIAdminPermission,)
