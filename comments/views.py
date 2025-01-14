from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CommentSerializer
from .models import  Comments


@api_view(['POST'])
def create(request):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Comment created successfully', 'data': serializer.data},status=status.HTTP_201_CREATED)
    return Response({'error': 'Invalid data', 'details': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_all(request):
    comments = Comments.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response({'data': serializer.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_comment(request, pk):
    try:
        comments = Comments.objects.get(pk=pk)
        serializer = CommentSerializer(comments)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    except Comments.DoesNotExist:
        return Response({'message': 'Comment does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def update_comment(request, pk):
    try:
        comments = Comments.objects.get(pk=pk)
        serializer = CommentSerializer(instance=comments, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Comments.DoesNotExist:
        return Response({'message': 'Comment does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_comment(request, pk):
    try:
        comment = Comments.objects.get(pk=pk)
        comment.delete()
        return Response({'message': 'Comment deleted successfully'}, status=status.HTTP_200_OK)
    except Comments.DoesNotExist:
        return Response({'message': 'Comment does not exist'}, status=status.HTTP_404_NOT_FOUND)
