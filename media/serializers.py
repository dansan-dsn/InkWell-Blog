from rest_framework import serializers
from .models import Media

def validate_file_type(value):
    allowed_types = ['image/jpeg', 'image/jpg', 'image/png', 'video/mp4', 'video/x-matroska', 'video/avi', 'video/mov']
    # Access the content_type directly from the file object
    if value.content_type not in allowed_types:
        raise serializers.ValidationError("Unsupported file type.")
    return value

class MediaSerializer(serializers.ModelSerializer):
    file = serializers.FileField(validators=[validate_file_type])

    class Meta:
        model = Media
        fields = '__all__'
