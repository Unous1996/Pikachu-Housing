from rest_framework import serializers
from users.models import UserProfile
from django.contrib.auth.models import User
from housing.models import House
from department.models import Department
from department.api.serializers import DepartmentSerializer
from distance.models import Distance
from like.models import Like

class UserProfileSerializer(serializers.ModelSerializer):
    viewed_house = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = (
            'department',
            'viewed_house',
        )

    def get_viewed_house(self, obj):
        return [house.name for house in obj.viewed_houses.all()]

class UserHouseSerializer12(serializers.ModelSerializer):
    like_count = serializers.SerializerMethodField()
    closest_department = serializers.SerializerMethodField()
    reason = serializers.SerializerMethodField()

    def get_like_count(self, obj):
        count = Like.objects.filter(house_id = obj.id).count()
        return count

    def get_closest_department(self, obj):
        department_set = Department.objects.raw('SELECT * FROM department_department WHERE id = %s', [int(obj.closest_department_float)])
        distance_set = Distance.objects.raw('SELECT * FROM distance_distance WHERE distance_distance.house_id_id = %s ORDER BY distance_distance.distance ASC',[obj.id,])

        for item in department_set:
            serializer = DepartmentSerializer(item)
            serialized_data = serializer.data

        for item in distance_set:
            serialized_data['distance'] = item.distance
            return serialized_data

    def get_reason(self, obj):
        if(self.get_like_count(obj)>=3):
            return ('close to department','cheap house', 'hot house')
        else:
            return ('close to department','cheap house')

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
            'like_count',
            'reason'
        )

class UserHouseSerializer13(serializers.ModelSerializer):
    like_count = serializers.SerializerMethodField()
    closest_department = serializers.SerializerMethodField()
    reason = serializers.SerializerMethodField()

    def get_like_count(self, obj):
        count = Like.objects.filter(house_id = obj.id).count()
        return count

    def get_closest_department(self, obj):
        department_set = Department.objects.raw('SELECT * FROM department_department WHERE id = %s', [int(obj.closest_department_float)])
        distance_set = Distance.objects.raw('SELECT * FROM distance_distance WHERE distance_distance.house_id_id = %s ORDER BY distance_distance.distance ASC',[obj.id,])

        for item in department_set:
            serializer = DepartmentSerializer(item)
            serialized_data = serializer.data

        for item in distance_set:
            serialized_data['distance'] = item.distance
            return serialized_data

    def get_reason(self, obj):
        return ('close to department', 'hot house')

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
            'like_count',
            'reason'
        )

class UserHouseSerializer23(serializers.ModelSerializer):
    like_count = serializers.SerializerMethodField()
    closest_department = serializers.SerializerMethodField()
    reason = serializers.SerializerMethodField()

    def get_like_count(self, obj):
        count = Like.objects.filter(house_id = obj.id).count()
        return count

    def get_closest_department(self, obj):
        department_set = Department.objects.raw('SELECT * FROM department_department WHERE id = %s', [int(obj.closest_department_float)])
        distance_set = Distance.objects.raw('SELECT * FROM distance_distance WHERE distance_distance.house_id_id = %s ORDER BY distance_distance.distance ASC',[obj.id,])

        for item in department_set:
            serializer = DepartmentSerializer(item)
            serialized_data = serializer.data

        for item in distance_set:
            serialized_data['distance'] = item.distance
            return serialized_data

    def get_reason(self, obj):
        return ('cheap house', 'hot house')

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
            'like_count',
            'reason'
        )

class UserSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    email = serializers.ReadOnlyField()
    username = serializers.CharField()
    # username = serializers.SerializerMethodField()
    profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'profile', 'is_superuser')


class SigninSerializer(serializers.Serializer):
    username_or_email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=100)
    remember = serializers.NullBooleanField(default=False)


class SignUpSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=100)
    department = serializers.IntegerField(default=-1)
    remember = serializers.NullBooleanField(default=False)
