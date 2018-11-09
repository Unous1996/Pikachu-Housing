from distance.models import Distance
from distance.api.paginations import DistancePagination
from serializers import DistanceSerializer
from rest_framework import viewsets, generics
from rest_framework.response import Response

class DistanceViewSet(viewsets.ModelViewSet):
    #pagination_class = DistancePagination
    model = Distance
    serializer_class = DistanceSerializer
    queryset = ''

    def list(self, request):
        queryset = Distance.objects.raw('SELECT * FROM distance_distance')
        serializers = DistanceSerializer(queryset, many=True)
        return Response(serializers.data)

    def retrieve(self, request, pk):
        queryset = Distance.objects.raw('SELECT * FROM distance_distance WHERE distance_distance.id = %s',[pk])
        serializers = DistanceSerializer(queryset, many=True)
        return Response(serializers.data)
