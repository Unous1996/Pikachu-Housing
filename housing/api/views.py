from rest_framework import viewsets
from housing.models import House
from housing.api.paginations import HousePagination
from serializers import HouseSerializer, ClosestHouseSerializer
from rest_framework import permissions
from rest_framework.response import Response
from itertools import chain

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
    queryset = ''

    def retrieve(self, request, pk):
        all_houses = House.objects.all()
        none_houses = House.objects.none()
        my_obj_list = []

        for obj in all_houses:
            closest = obj.get_closest_deptid()
            if closest == float(pk):
                my_obj_list.append(obj)
        print(my_obj_list)
        qs = list(chain(none_houses, my_obj_list))
        serializers = HouseSerializer(qs, many=True)
        return Response(serializers.data)
