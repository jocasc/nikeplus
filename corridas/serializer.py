from rest_framework import serializers
from corridas.models import Running, Distance


class RunningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Running
        fields = '__all__'


class DistanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distance
        fields = '__all__'