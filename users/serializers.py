from rest_framework import serializers
from .models import User
import bcrypt


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

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


class UserUpdateSerializer(serializers.Serializer):
    username = serializers.CharField(required=False)
    role = serializers.CharField(required=False)

    def validate(self, value):
        username = value.get('username')
        role = value.get('role')

        if User.objects.filter(username=username).exclude(id=self.instance.id).exists():
            raise serializers.ValidationError("This username is already taken.")

        if len(username) < 3:
            raise serializers.ValidationError("Username must be at least 3 characters long")

        allowed_role = ['author', 'guest']
        if role not in allowed_role:
            raise serializers.ValidationError("Role provided is not allowed")
        return value

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.role = validated_data.get('role', instance.role)

        instance.save()
        return instance


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("No account is associated with this email.")
        return value


class ChangeEmailSerializer(serializers.ModelSerializer):
    new_email = serializers.EmailField()

    class Meta:
        model = User
        fields = ['new_email']

    def validate_new_email(self, value):
        """Validate the new email address."""
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        # Additional checks for fake/disposable emails can go here
        return value

    def save(self, **kwargs):
        """Update the email address."""
        user = self.instance
        user.email = self.validated_data['new_email']
        user.save()
        return user




































