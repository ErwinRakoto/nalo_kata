"""
Url list
"""

from django.conf.urls import url, include
from rest_framework_nested import routers

from nalo.ice_cream_app.views import (
    IceBowlViewSet
)

ROUTER = routers.SimpleRouter()
ROUTER.register(r'icebowl', IceBowlViewSet, basename='icb')


urlpatterns = [
    url(r'^', include(ROUTER.urls)),
]
