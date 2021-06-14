from rest_framework import serializers
from rest_api_board.models import MyBoard
from django.contrib.auth.models import User

#Board REST Api
class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyBoard
        fields = ('id', 'subject', 'create_by', 'create_at', 'content')

