from rest_framework import routers
from django.conf.urls import include, url, patterns
from housing.api.views import BlogViewSet

router = routers.DefaultRouter()
router.register(r'blog', BlogViewSet, base_name='blog')

app_name = 'api'

urlpatterns = patterns(
    'api',
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework'))

)
