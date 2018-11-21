from rest_framework import viewsets
from housing.models import House
from housing.api.paginations import HousePagination
from serializers import HouseSerializer, HouseSerializerPruned
from rest_framework import permissions
from rest_framework.response import Response

class HouseViewSet(viewsets.ModelViewSet):
    pagination_class = HousePagination
    serializer_class = HouseSerializer
    permission_classes = (permissions.BasePermission,)

    def get_queryset(self):
        queryset = House.objects.all()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class ClosestHouseViewSet(viewsets.ModelViewSet):
    pagination_class = HousePagination
    serializer_class = HouseSerializer
    permission_classes = (permissions.BasePermission,)

    def retrieve(self, request, pk):
    	house_raw_set = House.objects.raw('SELECT * FROM housing_house')
        #use the method in the model, the internet is not so good 
    	serializers = HouseSerializer(house_raw_set, many=True)
    	return Response(serializers.data)
