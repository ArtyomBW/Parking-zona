from http import HTTPStatus

from django.http import JsonResponse
from drf_spectacular.utils import extend_schema
from drf_spectacular.views import SpectacularAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from user.models import User
from user.serializers import RegisterModelSerializer, ForgotSerializer, VerifyOTPSerializer, \
    ChangePasswordSerializer


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
            return JsonResponse({'status': HTTPStatus.ACCEPTED, "message": "Parol o'zgartirildi"})
        return JsonResponse({'status': HTTPStatus.BAD_REQUEST, "message": serializer.errors})






























