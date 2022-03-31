from rest_framework import viewsets
from corridas.models import Running, Distance
from corridas.serializer import RunningSerializer, DistanceSerializer


class RunningViewSet(viewsets.ModelViewSet):
    '''exibindo todas as corridas'''
    queryset = Running.objects.all()
    serializer_class = RunningSerializer


class DistanceViewSet(viewsets.ModelViewSet):
    '''exibindo todas as corridas'''
    queryset = Distance.objects.all()
    serializer_class = DistanceSerializer

