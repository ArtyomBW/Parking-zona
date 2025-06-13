from django.urls import path

from user.views import *




# =-=-=-=-=-=-=-=-=-=-=-=-=-= Auth =-=-=-=-=-=-=-=-=-=-=-=-=-=

urlpatterns = [
    path('register' , RegisterCreateAPIView.as_view()),
    path('forgot_password' , ForgotAPIView.as_view()),
    path('verify_otp' , VerifyOTPAPIView.as_view()),
    path('change_password' , ChangePasswordAPIView.as_view()),
    ]



# =-=-=-=-=-=-=-=-=-=-=-=-=-= Profile =-=-=-=-=-=-=-=-=-=-=-=-=-=

urlpatterns += [
    path('profile/about', ProfileAPIView.as_view()),
    path('profile/update', ProfileUpdateAPIView.as_view()),
    path('profile/list', ProfileListAPIView.as_view()),
    path('profile/<int:pk>', ProfileDeleteAPIView.as_view())
]
