from django.urls import path, include
from .views import CityViewSet, SubscribeViewSet, UserSubscribesListView
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'city', CityViewSet)
router.register(r'subscribe', SubscribeViewSet)


urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/subscribe/user-list', UserSubscribesListView.as_view())
]