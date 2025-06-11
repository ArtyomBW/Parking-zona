import json
import random
import re
from datetime import timedelta

from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from redis import Redis
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer, Serializer

from root.settings import EMAIL_HOST_USER
from user.models import User


class RegisterModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = 'username', 'email', 'password', 'phone', 'first_name'

    def validate_password(self, value):
        return make_password(value)

    def validate_phone(self, value):
        return re.sub(r'\D', '',value)  # re kutubxona D = Digit , '' = bosh joy faqat sonlar qoladi


class ForgotSerializer(Serializer):         # Forgot password uchun emailga xabar berish
    email = CharField(max_length=255, )
    def validate_email(self, value):
        query = User.objects.filter(email=value)
        if not query.exists():
            raise ValidationError("Bu gmail topilmadi ...")
        return value


    def send_cod(self, email):   # Random code yaratish va yuborish
        redis = Redis(decode_responses=True)
        code = str(random.randint(10**5, 10**6))
        data = {"code" : code, "status": False}
        data_str = json.dumps(data)
        redis.mset({email: data_str})
        redis.expire(email, timedelta(minutes=3))
        send_mail("Very code:", code,
            EMAIL_HOST_USER,[email])

class VerifyOTPSerializer(Serializer):                # Kodni qabul qilish uchun
    email = CharField(max_length=255)
    code = CharField(max_length=12)

    def validate(self, attrs):
        redis = Redis(decode_responses=True)
        email = attrs.get('email')
        code = attrs.get('code')
        data_str = redis.mget(email)[0]

        if not data_str:
            raise ValidationError("Kod yuborilmagan ...")
        data_dict:dict = json.loads(data_str)           # str -> dict
        verify_code = data_dict.get('code')                 #

        if str(verify_code) != str(code):
            raise ValidationError("Notog'ri parol ...")
        redis.mset({email: json.dumps({"status": "True"})})
        redis.expire(email, time=timedelta(minutes=3))
        return attrs


class ChangePasswordSerializer(Serializer):
    email = CharField(max_length=255)
    password = CharField(max_length=128)
    confirm_password = CharField(max_length=12)

    def validate_email(self, value):
        redis = Redis(decode_responses=True)
        data_str = redis.mget(value)[0]         # dict --> str

        if not data_str:                        # Error shu erda
            raise ValidationError("Kod yuborilmagan yoki muddati tugagan ...")

        try:
            data_dict:dict = json.loads(data_str)
        except json.JSONDecodeError:
            raise ValidationError("Notog'ri ma'lumot formati ...")

        status = data_dict.get('status')
        if status == "False":
            raise ValidationError("Emailni tasdiqlang ...")
        redis.delete(value)
        return value

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        if password != confirm_password:
            raise ValidationError("Tasdiqlash paroli bir xil emas ...")
        attrs['password'] = make_password(password)
        return attrs

    def save(self, **kwargs):
        data = self.validated_data
        email = data.get('email')
        password = data.get('password')
        User.objects.filter(email=email).update(password=password)








