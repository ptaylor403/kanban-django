from rest_framework import viewsets
from .models import Faketrello
from .serializers import FaketrelloSerializer


class FaketrelloViewSet(viewsets.ModelViewSet):
    queryset = Faketrello.objects.all().order_by('title')
    serializer_class = FaketrelloSerializer
