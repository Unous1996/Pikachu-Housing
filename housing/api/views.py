from rest_framework import viewsets
from housing.models import House
from housing.api.paginations import HousePagination
from serializers import HouseSerializer


class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    pagination_class = HousePagination
    serializer_class = HouseSerializer
