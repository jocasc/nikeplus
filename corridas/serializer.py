from rest_framework import serializers
from corridas.models import Running, Distance


class RunningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Running
        fields = ['name', 'description', 'total_distance', 'running_start', 'running_end',
                  'elapsed_time', 'calories', 'cadence', 'elevation_gain', 'elevation_loss']


class DistanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distance
        fields = '__all__'#['avg_pace', 'elevation']