from rest_framework import viewsets
from department.models import Department
from department.api.paginations import DepartmentPagination
from serializers import DepartmentSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    pagination_class = DepartmentPagination
    serializer_class = DepartmentSerializer
