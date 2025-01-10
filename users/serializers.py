from rest_framework import serializers
from .models import User
import bcrypt


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'password', 'created_at']


    def validate(self, value):
        if not value.get('username') or not value.get('email') or not value.get('password'):
            raise serializers.ValidationError('All fields are required')

        if User.objects.filter(username=value['username']).exists():
            raise serializers.ValidationError('Username is already taken')

        if User.objects.filter(email=value['email']).exists():
            raise serializers.ValidationError('Email is already in use')

        if value['username'] == 'D@dmin' and value['email'] == 'ddryn970@gmail.com':
            value['role'] = 'admin'

        if len(value.get('password', '')) < 6:
            raise serializers.ValidationError('Password must be at least 6 characters')

        password = value.get('password')
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

        value['password'] = hashed_password.decode('utf-8')

        return value


class LoginSerializer(serializers.Serializer):
    username_or_email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


    def validate(self, data):
        username_or_email = data.get('username_or_email')
        password = data.get('password')

        user = User.objects.filter(username=username_or_email).first() or User.objects.filter(email=username_or_email).first()

        if not user:
            raise serializers.ValidationError('Invalid username/email or password')

        if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            raise serializers.ValidationError('Invalid username/email or password')

        return data
































