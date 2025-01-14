from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import BlogSerializer, BlogUpdateSerializer
from .models import Blog


@api_view(['POST'])
def create_blog(request):
    serializer = BlogSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Blog Post created successfully', 'details': serializer.data}, status=status.HTTP_201_CREATED)
    return Response({'error': 'Invalid data', 'details': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_blogs(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return  Response({'data': serializer.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_blog(request, pk):
    try:
        blog = Blog.objects.get(pk=pk)
        serializer = BlogSerializer(blog)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    except Blog.DoesNotExist:
        return Response({'message': 'Blog post not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def update_blog(request, pk):
    try:
        blog = Blog.objects.get(pk=pk)
        serializer = BlogUpdateSerializer(blog, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Blog Post updated successfully', 'details': serializer.data}, status=status.HTTP_200_OK)
        return Response({'message': 'Invalid data','error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Blog.DoesNotExist:
        return Response({'message': 'Blog Post not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_blog(request, pk):
    try:
        blog = Blog.objects.get(pk=pk)
        blog.delete()
        return Response({'message': 'Blog post deleted successfully'}, status=status.HTTP_200_OK)
    except Blog.DoesNotExist:
        return Response({'message':'Blog post not found'}, status=status.HTTP_404_NOT_FOUND)