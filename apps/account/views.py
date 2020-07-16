from rest_framework import viewsets, status
from rest_framework.response import Response
from apps.account import models, serializers
from apps.account.models import User
from apps.account.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request):

        last_user = models.User.objects.all()[:5]

        serializer = serializers.UserSerializer(last_user, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
