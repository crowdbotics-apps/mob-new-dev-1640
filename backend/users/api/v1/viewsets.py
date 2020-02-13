from rest_framework import authentication
from users.models import Test
from .serializers import TestSerializer
from rest_framework import viewsets


class TestViewSet(viewsets.ModelViewSet):
    serializer_class = TestSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Test.objects.all()
