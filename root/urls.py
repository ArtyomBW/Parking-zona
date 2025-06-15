


from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView
from rest_framework.routers import SimpleRouter

from user.views import CustomTokenRefreshView, CustomTokenObtainPairView, CustomSpectacularAPIView, \
    ParkingZoneModelViewSet

urlpatterns = [
    # DRF schema va swagger
    path('api/schema/', CustomSpectacularAPIView.as_view(), name='schema'),
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # Admin va API auth
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('user.urls')),

    # JWT token view lar
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),

]
# =-=-=-=-=-=-=-=-=-=-=-=-=-= ZONA CONFIG =-=-=-=-=-=-=-=-=-=-=-=-=-=

zones = SimpleRouter()
zones.register(r'parking-zones', ParkingZoneModelViewSet)
urlpatterns += zones.urls






