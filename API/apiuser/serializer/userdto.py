from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

class UserSerializer(serializers.Serializer):
    password = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()


    
    def validate(self, validated_data):
        password=validated_data['password'],
        username=validated_data['username'],
        email=validated_data['email']
        return validated_data
