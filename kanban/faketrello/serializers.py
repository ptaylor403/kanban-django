from rest_framework import serializers
from .models import Faketrello


class FaketrelloSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Faketrello
        fields = ('user', 'title', 'description', 'priority')
