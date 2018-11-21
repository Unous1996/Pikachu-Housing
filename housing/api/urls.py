from housing.api import views
from rest_framework.urlpatterns import format_suffix_patterns
from housing.api.views import ClosestHouseViewSet

housing_detail = ClosestHouseViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
	url(r'^$', views.api_root, name='api_root'),
	url(r'^house/department/(?P<pk>[0-9]+)/$', housing_detail, name='housing-detail'),
])