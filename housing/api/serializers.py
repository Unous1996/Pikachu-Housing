from rest_framework import serializers
from housing.models import House
from distance.models import Distance
from rest_framework.response import Response
from django.http import JsonResponse
from department.api.serializers import DepartmentSerializer

class HouseSerializer(serializers.ModelSerializer):

    closest_department = serializers.SerializerMethodField()

    def get_closest_department(self, obj):

        distance_set = Distance.objects.raw('SELECT * FROM distance_distance WHERE distance_distance.house_id_id = %s ORDER BY distance_distance.distance ASC',[obj.id,])

        for item in distance_set:
            serializer = DepartmentSerializer(item.department_id)
            serialized_data = serializer.data
            serialized_data['distance'] = item.distance
            return serialized_data

    class Meta:
        model = House
        fields = (
            'id',
            'name',
            'price',
            'location',
            'cover_img',
            'types',
            'description',
            'imgs_url',
            'latitude',
            'longitude',
            'provider',
            'closest_department',
        )


class ClosestHouseSerializer(serializers.ModelSerializer):

    is_closest = serializers.SerializerMethodField('_is_closest')

    def _is_closest(self, obj):
        target_dept = self.context.get('department_id')
        if target_dept:
            return target_dept == self.get_closest_department()
        return False

    def get_is_closest(self):
        query_set = House.objects.filter(_is_closest=True)
        serializer = HouseSerializer(query_set, many=True)
        return serializer.data

    class Meta:
        model = House
        fields = (
            'id',
            'name',
            'price',
            'location',
            'cover_img',
            'types',
            'description',
            'imgs_url',
            'latitude',
            'longitude',
            'provider',
            'is_closest'
        )


