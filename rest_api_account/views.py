from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import status

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
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
            return Response({"Token": token.key})
        else:
            return Response("넌 로그인할 자격이 없다.", status.HTTP_401_UNAUTHORIZED)
