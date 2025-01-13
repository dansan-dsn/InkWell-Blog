from django.utils.text import slugify
from rest_framework import serializers
from .models import Blog
from users.models import User


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'slug', 'content', 'author', 'published_date']

    def validate(self, data):
        author = data.get('author')
        if not author:
            raise serializers.ValidationError({'author': 'Author is required.'})

        try:
            user = User.objects.get(id=author.id)
            if user.role == 'guest':
                raise serializers.ValidationError({'author': 'User not allowed to create a blog post'})
        except User.DoesNotExist:
            raise serializers.ValidationError({'author': 'User not found'})

        if not data.get('slug'):
            title = data.get('title', '')
            slug = slugify(title)
            data['slug'] = slug

            existing_slug = Blog.objects.filter(slug=data['slug']).exists()
            if existing_slug:
                data['slug'] = f"{data['slug']}-{Blog.objects.count() + 1}"

        return data

    def to_representation(self, instance):
        rep = super().to_representation(instance)

        author = instance.author
        rep['author'] = {
            'username': author.username,
            'role': author.role,
        }

        return rep


class BlogUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    slug = serializers.CharField(required=False)
    content = serializers.CharField(required=False)


    def validate(self, data):
        if 'title' in data:
            title = data['title']
            slug = slugify(title)
            data['slug'] = slug

            existing_slug = Blog.objects.filter(slug=slug).exists()
            if existing_slug:
                data['slug'] = f"{slug}-{Blog.objects.count() + 1}"

        return data


    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.content = validated_data.get('content', instance.content)

        instance.save()
        return instance