from rest_framework import serializers
from .models import User
import django.contrib.auth.password_validation as validators

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ["id", "email", "status", "password"]
    
    #Password validator для кастомного пользователя
    def validate(self, data):
        password = data.get('password')
        
        validators.validate_password(password=password)
        
        return super(UserSerializer, self).validate(data)    
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user