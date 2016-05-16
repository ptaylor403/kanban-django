from rest_framework import serializers
from .models import Faketrello


class FaketrelloSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Faketrello
        fields = ('url', 'user', 'title', 'description', 'priority')
