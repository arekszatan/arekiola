
from django.urls import path, include
from rest_framework import routers
from .views import PostViewSet, index

router = routers.DefaultRouter()
router.register(r'upload', PostViewSet, basename="upload")

# Wire up our API using automatic URL routing.
urlpatterns = [
    path('dreams/', index, name='index'),
    path('api/dreams/uploadFile', include(router.urls)),
]
