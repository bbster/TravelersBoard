from rest_framework import serializers

from apps.account.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        fields = (
            'id',
            'username',
            'password',
            'email'
        )
