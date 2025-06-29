from http import HTTPStatus

from django.http import JsonResponse
from drf_spectacular.utils import extend_schema
from drf_spectacular.views import SpectacularAPIView
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from user.models import User, ParkingZone
from user.permissions import IsAdmin
from user.serializers import RegisterModelSerializer, ForgotSerializer, VerifyOTPSerializer, \
    ChangePasswordSerializer, ProfileModelSerializer, ParkingZoneSerializer


@extend_schema(tags=['Auth'])
class CustomSpectacularAPIView(SpectacularAPIView):
    pass
@extend_schema(tags=['Auth'])
class CustomTokenObtainPairView(TokenObtainPairView):
    pass
@extend_schema(tags=['Auth'])
class CustomTokenRefreshView(TokenRefreshView):
    pass

@extend_schema(tags=['Auth'])
class RegisterCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterModelSerializer

@extend_schema(tags=['Auth'], request=ForgotSerializer)
class ForgotAPIView(APIView):
    def post(self, request):
        data = request.data
        serializer = ForgotSerializer(data=data)
        if serializer.is_valid():
            serializer.send_cod(data['email'])
            return JsonResponse ({'status': HTTPStatus.ACCEPTED, "message": "Kod yuborldi >>>"})
        return JsonResponse({'status': HTTPStatus.BAD_REQUEST, "message": "Foydalanuvchi topilmadi :("})

@extend_schema(tags=['Auth'], request=VerifyOTPSerializer)
class VerifyOTPAPIView(APIView):
    def post(self, request):
        data = request.data
        serializer = VerifyOTPSerializer(data=data)
        if serializer.is_valid():
            return JsonResponse({'status': HTTPStatus.ACCEPTED, "message": "Kod qabul qilindi"})
        return JsonResponse({'status': HTTPStatus.BAD_REQUEST, "message":  serializer.errors })

@extend_schema(tags=['Auth'], request=ChangePasswordSerializer)
class ChangePasswordAPIView(APIView):
    def post(self, request):
        data = request.data
        serializer = ChangePasswordSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'status': HTTPStatus.ACCEPTED, "message": "Parol muvaffaqiyatli o'zgartirildi"})
        return JsonResponse({'status': HTTPStatus.BAD_REQUEST, "message": serializer.errors})


@extend_schema(tags=['Profile'], responses=ProfileModelSerializer)
class ProfileAPIView(APIView):
    def get(self, request):
        user = request.user
        serializers = ProfileModelSerializer(instance=user)
        return JsonResponse({"status": HTTPStatus.OK, "user": serializers.data})

@extend_schema(tags=['Profile'], request=ProfileModelSerializer)
class ProfileUpdateAPIView(UpdateAPIView):
    serializer_class = ProfileModelSerializer
    def get_object(self):
        return self.request.user

@extend_schema(tags=['Profile'], responses=ProfileModelSerializer)
class ProfileListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileModelSerializer
    permission_classes = [IsAdmin]

@extend_schema(tags=['Profile'], )
class ProfileDeleteAPIView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileModelSerializer
    permission_classes = [IsAdmin]

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-  Parking Zona  =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

@extend_schema(tags=['parking-zones'])
class ParkingZoneModelViewSet(viewsets.ModelViewSet):
    queryset = ParkingZone.objects.all()
    serializer_class = ParkingZoneSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated]
        return [IsAdmin()]

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-  Pa Zona  =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

