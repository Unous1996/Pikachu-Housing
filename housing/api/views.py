from rest_framework import viewsets
from housing.models import House
from housing.api.paginations import HousePagination
from serializers import HouseSerializer


class HouseViewSet(viewsets.ModelViewSet):
    pagination_class = HousePagination
    serializer_class = HouseSerializer

    def get_queryset(self):
        queryset = House.objects.all()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        return queryset
