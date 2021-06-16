from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import status

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Profiles
from . import models


class SignupView(APIView):
    def post(self, request):
        user = User.objects.create_user(username=request.data['id'], password=request.data['password'])
        profile = models.Profiles(user=user, nickname=request.data['nickname'])
        user.save()
        profile.save()
        token = Token.objects.create(user=user)
        return Response({"Token": token.key})


class LoginView(APIView):
    def post(self, request):
        user = authenticate(username=request.data['id'], password=request.data['password'])
        if user is not None:
            token = Token.objects.get(user=user)
            pro = Profiles.objects.filter(user=user).values()
            # pro[0].get('nickname')
            response = Response()
            response.set_cookie(key="Token", value=token.key)
            response.set_cookie(key="nickname", value=pro[0].get('nickname'))
            response.data = {
                "Token": token.key,
                "nickname": pro[0].get('nickname'),
            }
            return response
        else:
            return Response("넌 로그인할 자격이 없다.", status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    def get(self, request):
        response = Response()
        response.delete_cookie('Token')
        response.delete_cookie('nickname')
        return response
