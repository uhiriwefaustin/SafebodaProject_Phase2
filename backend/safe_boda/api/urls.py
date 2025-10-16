from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TripViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'trips', TripViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # <- include the API
]
