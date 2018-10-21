from rest_framework import serializers
from housing.models import House


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = (
            'id',
            'name',
            'price',
            'imgs_url',
            'types',
        )
