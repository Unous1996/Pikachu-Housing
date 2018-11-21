from rest_framework import serializers
from housing.models import House
from distance.models import Distance
class HouseSerializer(serializers.ModelSerializer):

    closest_department_id = serializers.SerializerMethodField()
    closest_department_name = serializers.SerializerMethodField()

    def get_closest_department_id(self, obj):
        distance_set = Distance.objects.raw('SELECT * FROM distance_distance WHERE distance_distance.house_id_id = %s ORDER BY distance_distance.distance ASC',[obj.id,])
        for item in distance_set:
            return item.department_id.id
        return None

    def get_closest_department_name(self, obj):
        distance_set = Distance.objects.raw('SELECT * FROM distance_distance WHERE distance_distance.house_id_id = %s ORDER BY distance_distance.distance ASC',[obj.id,])
        for item in distance_set:
            return item.department_id.name
        return None

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
            'closest_department_id',
            'closest_department_name'
        )
