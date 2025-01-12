from django.utils.text import slugify
from rest_framework import serializers
from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'slug', 'content', 'author', 'published_date']


    def validate(self, data):
        if not data.get('slug'):
            title = data.get('title', '')
            slug = slugify(title)
            data['slug'] = slug

            existing_slug = Blog.objects.filter(slug=data['slug']).exists()
            if existing_slug:
                data['slug'] = f"{data['slug']}-{Blog.objects.count() + 1}"

        return data
