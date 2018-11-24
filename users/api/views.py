from rest_framework import viewsets,status, serializers
from users.models import UserProfile
from django.contrib.auth.models import User, BaseUserManager
from users.api.paginations import UserPagination
from users.api.serializers import UserSerializer, UserProfileSerializer, SigninSerializer, SignUpSerializer, UserHouseSerializer12, UserHouseSerializer13, UserHouseSerializer23
from users.api.service import UserService
from users.api.permissions import UserPermission
from rest_framework import permissions
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import login as django_login, authenticate, logout as django_logout
from django.utils import timezone
from department.models import Department
from housing.models import House
from housing.api.serializers import HouseSerializer
from like.models import Like
from itertools import chain

def get_like_count(house_obj):
    count = Like.objects.filter(house_id = house_obj.id).count()
    return count

class UserProfileViewSet(viewsets.ModelViewSet):
    pagination_class = UserPagination
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.BasePermission,)

    def get_queryset(self):
        queryset = UserProfile.objects.all()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        return queryset

class UserViewset(viewsets.ModelViewSet):
    pagination_class = UserPagination
    serializer_class = UserSerializer
    permission_classes = (UserPermission, IsAuthenticated)

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset

    @list_route(methods=['GET'])
    def profile(self, request):
        return Response(self.get_serializer(request.user).data)

    @list_route(methods=['GET'])
    def logout(self, request):
        django_logout(request)
        return Response({'next': '/'}, status=status.HTTP_200_OK)

    @detail_route(methods=['GET'])
    def suggestion(self, request, pk=None):
        #1:close_to_department 
        #2:cheap_house
        #3:hot_house
        cheap_thereshold = 600
        count_threshold = 3

        pk_int = int(pk[1:])
        user= User.objects.raw("SELECT * FROM auth_user WHERE id = %s",[pk_int])
        department_float = -1.0
        for user_item in user:
            department_float = float(user_item.profile.department.id) 
        
        queryset_1 = House.objects.raw('SELECT * FROM housing_house WHERE closest_department_float = %s',[department_float])
        queryset_2 = House.objects.raw('SELECT * FROM housing_house WHERE price < %s',[cheap_thereshold])
        
        set_1 = set(queryset_1)
        set_2 = set(queryset_2)
        set_12 = set_1.intersection(set_2)
        set_1not2 = set_1.difference(set_12)
        set_2not1 = set_2.difference(set_12)
        
        queryset_i12 = list(set_12)
        queryset_1not2 = list(set_1not2)
        queryset_2not1 = list(set_2not1)

        queryset_13_list = []
        queryset_23_list = []

        qs_none = House.objects.none()

        for item in queryset_1not2:
            if get_like_count(item) >= count_threshold:
                queryset_13_list.append(item)

        for item in queryset_2not1:
            if get_like_count(item) >= count_threshold:
                queryset_23_list.append(item)

        queryset_i13 = list(chain(qs_none, queryset_13_list))
        queryset_i23 = list(chain(qs_none, queryset_23_list))

        serializer12 = UserHouseSerializer12(queryset_i12, many=True)
        serializer13 = UserHouseSerializer13(queryset_i13, many=True)
        serializer23 = UserHouseSerializer23(queryset_i23, many=True)
        '''
        queryset_w13_raw = House.objects.raw('SELECT * FROM housing_house WHERE closest_department_float = %s AND price >= %s',[department_float, cheap_thereshold])
        qs_none = House.objects.none()
        queryset_w13_filtered_list = []
        for item in queryset_w13_raw:
            if get_like_count(item) >= 3:
                queryset_w13_filtered_list.append(item)
        queryset_w13_filtered = list(chain(qs_none, queryset_w13_filtered_list))
        serializer13 = UserHouseSerializer13(queryset_w13_filtered, many=True)
        '''
        Serializer_list = [serializer12.data, serializer13.data, serializer23.data]
        content = {
            'status': 1,
            'responseCode' : status.HTTP_200_OK, 
            'data': Serializer_list
        }
        
        return Response(content)

    @list_route(methods=['POST'], permission_classes=[AllowAny])
    def signin(self, request):
        serializer = SigninSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        username_or_email = serializer.data['username_or_email']
        password = serializer.data['password']
        user = UserService.get_user_by_username_or_email(username_or_email)
        if not user:
            error = 'Username or email does not exist.'
            return Response({'error': error}, status=status.HTTP_401_UNAUTHORIZED)

        user.backend = 'django.contrib.auth.backends.ModelBackend'
        django_login(request, user)
        remember = serializer.data['remember']
        if not remember:
            request.session.set_expiry(0)
        else:
            request.session.set_expiry(60 * 60 * 24 * 60)

        next = request.GET.get('next', '')
        if next == '':
            next = '/problem/'
        return Response({'next': next}, status=status.HTTP_200_OK)

    @list_route(methods=['POST'], permission_classes=[AllowAny])
    def signup(self, request):
        serializer = SignUpSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        email = serializer.data['email']
        password = serializer.data['password']
        username = serializer.data['username']
        department_id = serializer.data['department']
        email = BaseUserManager.normalize_email(email)
        user = UserService.get_user_by_username_or_email(email)
        if user:
            return Response({'error': "Email has been used"}, status=status.HTTP_401_UNAUTHORIZED)
        now = timezone.now()
        user = User.objects.create(email=email, username=username,
                                   is_staff=False, is_superuser=False, is_active=True,
                                   last_login=now, date_joined=now)
        user.set_password(password)
        profile = UserProfile.objects.create(user=user)
        if department_id:
            depart = Department.objects.get(id=department_id)
            profile.department = depart

        user.save()
        profile.save()
        return Response({'message': 'Create user successfully'}, status=status.HTTP_200_OK)

