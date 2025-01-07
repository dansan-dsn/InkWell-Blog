from rest_framework import serializers
from .models import  User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username', 'email', 'role', 'password', 'created_at']

    def validate_user(self, data):
        if User.objects.filter(username=data).exists():
            raise serializers.ValidationError('Username not available')
        if User.objects.filter(email=data).exists():
            raise serializers.ValidationError('Email in use')
        return data

    def validate_password(self, value):
        if len(value) < 6:
            raise serializers.ValidationError('Password must be 6 characters long')

    def validate(self, value):
        if not value.get('username') or not value.get('email') or not value.get('password'):
            raise serializers.ValidationError('All fields are required')
        return value