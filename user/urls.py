from django.urls import path

from user.views import RegisterCreateAPIView, ForgotAPIView, VerifyOTPAPIView, ChangePasswordAPIView

urlpatterns = [
    path('register' , RegisterCreateAPIView.as_view()),
    path('forgot_password' , ForgotAPIView.as_view()),
    path('verify_otp' , VerifyOTPAPIView.as_view()),
    path('change_password' , ChangePasswordAPIView.as_view()),

]


