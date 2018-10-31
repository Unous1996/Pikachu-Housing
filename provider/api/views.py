from rest_framework import viewsets
from provider.models import Provider
from provider.api.paginations import ProviderPagination
from serializers import ProviderSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    pagination_class = ProviderPagination
    serializer_class = ProviderSerializer
