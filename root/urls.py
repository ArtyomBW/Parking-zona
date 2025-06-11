
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView
from user.views import CustomTokenRefreshView, CustomTokenObtainPairView, CustomSpectacularAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('user.urls')),
]


urlpatterns += [
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/', CustomSpectacularAPIView.as_view(), name='schema'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('login', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),

]

# =-=-=-=-=-=-=-=-=-=-=-=-=-= Thrid CONFIG =-=-=-=-=-=-=-=-=-=-=-=-=-=



