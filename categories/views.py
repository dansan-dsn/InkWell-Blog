from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CategoriesSerializer
from .models import  Categories


@api_view(['POST'])
def create(request):
    serializer = CategoriesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Category created successfully', 'data': serializer.data},status=status.HTTP_201_CREATED)
    return Response({'error': 'Invalid data', 'details': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_all(request):
    categories = Categories.objects.all()
    serializer = CategoriesSerializer(categories, many=True)
    return Response({'data': serializer.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_category(request, pk):
    try:
        category = Categories.objects.get(pk=pk)
        serializer = CategoriesSerializer(category)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    except Categories.DoesNotExist:
        return Response({'message': 'Category does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def update_category(request, pk):
    try:
        category = Categories.objects.get(pk=pk)
        serializer = CategoriesSerializer(instance=category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Categories.DoesNotExist:
        return Response({'message': 'Category does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_category(request, pk):
    try:
        category = Categories.objects.get(pk=pk)
        category.delete()
        return Response({'message': 'Category deleted successfully'}, status=status.HTTP_200_OK)
    except Categories.DoesNotExist:
        return Response({'message': 'Category does not exist'}, status=status.HTTP_404_NOT_FOUND)
