from distance.models import Distance
from distance.api.paginations import DistancePagination
from serializers import DistanceSerializer
from rest_framework import viewsets, generics


class DistanceViewSet(viewsets.ModelViewSet):
    pagination_class = DistancePagination
    serializer_class = DistanceSerializer

    def get_queryset(self):
        queryset = Distance.objects.all()
        return queryset

