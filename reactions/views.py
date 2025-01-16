from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ReactionSerializer
from .models import  Reaction


@api_view(['POST'])
def create(request):
    serializer = ReactionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Reaction created successfully', 'data': serializer.data},status=status.HTTP_201_CREATED)
    return Response({'error': 'Invalid data', 'details': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_all(request):
    reactions = Reaction.objects.all()
    serializer = ReactionSerializer(reactions, many=True)
    return Response({'data': serializer.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_reaction(request, pk):
    try:
        reaction = Reaction.objects.get(pk=pk)
        serializer = ReactionSerializer(reaction)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    except Reaction.DoesNotExist:
        return Response({'message': 'Reaction does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def update_reaction(request, pk):
    try:
        reaction = Reaction.objects.get(pk=pk)
        serializer = ReactionSerializer(instance=reaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Reaction.DoesNotExist:
        return Response({'message': 'Reaction does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_reaction(request, pk):
    try:
        reaction = Reaction.objects.get(pk=pk)
        reaction.delete()
        return Response({'message': 'Reaction deleted successfully'}, status=status.HTTP_200_OK)
    except Reaction.DoesNotExist:
        return Response({'message': 'Reaction does not exist'}, status=status.HTTP_404_NOT_FOUND)
