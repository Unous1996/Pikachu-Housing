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
            dept = item.department_id
            serializer = DepartmentSerializer(dept)
            return serializer.data
        return 

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
