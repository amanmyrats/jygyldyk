from django.contrib.auth import get_user_model

from rest_framework import serializers

# from api import settings
from django.conf import settings

User = get_user_model()


class AdminUserSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="admin-user-detail")
    date_joined = serializers.DateTimeField(read_only=True)

    class Meta:
        model = User
        fields = settings.ADMIN_USER_FIELDS
