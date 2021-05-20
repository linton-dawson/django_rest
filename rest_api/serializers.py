from rest_framework import serializers
from .models import Slot1, Slot2

class Slot1Serializer(serializers.HyperlinkedModelSerializer):
    invalid_trigger = serializers.CharField(default=None)
    key = serializers.CharField(default=None)
    support_multiple = serializers.BooleanField(default=True)
    pick_first = serializers.BooleanField(default=False)
    supported_values = serializers.ListField(child=serializers.CharField())
    values = serializers.ListField(child=serializers.DictField(child=serializers.CharField()))
    class Meta:
        model = Slot1
        fields = '__all__'

class Slot2Serializer(serializers.HyperlinkedModelSerializer):
    invalid_trigger = serializers.CharField(default=None)
    key = serializers.CharField(default=None)
    support_multiple = serializers.BooleanField(default=True)
    pick_first = serializers.BooleanField(default=False)
    type = serializers.ListField(child = serializers.CharField())
    constraint = serializers.CharField(default=None)
    var_name = serializers.CharField(default=None)
    values = serializers.ListField(child=serializers.DictField(child=serializers.CharField()))
    class Meta:
        model = Slot2
        fields = '__all__'