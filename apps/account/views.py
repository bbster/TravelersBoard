from rest_framework import viewsets, status
from rest_framework.response import Response
from apps.account import models, serializers


class UserViewSet(viewsets.ModelViewSet):

    def list(self, request):

        last_user = models.User.objects.all()[:5]

        serializer = serializers.UserSerializer(last_user, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
