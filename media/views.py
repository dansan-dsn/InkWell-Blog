from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Media
from .serializers import MediaSerializer

@api_view(['GET'])
def list_media(request):
    media = Media.objects.all().order_by('-uploaded_at')
    serializer = MediaSerializer(media, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_media(request):
    serializer = MediaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def retrieve_media(request, pk):
    try:
        media = Media.objects.get(pk=pk)
        serializer = MediaSerializer(media)
        return Response(serializer.data)
    except Media.DoesNotExist:
        return Response({'error': 'Media not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def update_media(request, pk):
    try:
        media = Media.objects.get(pk=pk)
        serializer = MediaSerializer(media, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Media.DoesNotExist:
        return Response({'error': 'Media not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_media(request, pk):
    try:
        media = Media.objects.get(pk=pk)
        media.delete()
        return Response({'message': 'Media deleted successfully'}, status=status.HTTP_200_OK)
    except Media.DoesNotExist:
        return Response({'error': 'Media not found'}, status=status.HTTP_404_NOT_FOUND)
