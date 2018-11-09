from rest_framework import viewsets
from users.models import UserProfile
from users.api.paginations import UserPagination
from users.api.serializers import UserProfileSerializer
from rest_framework import permissions


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
