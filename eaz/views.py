from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import get_object_or_404

from . models import Thing , Category
from . serializers import ThingSerializer,CategorySerializer,UserSerializer


@api_view(['GET'])
def category(request):
    queryset = Category.objects.all()
    serializer = CategorySerializer(queryset,many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def famous(request):
    queryset = Thing.objects.filter(category=1)
    serializer = ThingSerializer(queryset,many=True,context={'request':request})
    
    return Response(serializer.data)


@api_view(['GET'])
def foods(request):
    queryset = Thing.objects.filter(category=2)
    serializer = ThingSerializer(queryset,many=True,context={'request':request})
    
    return Response(serializer.data)

@api_view(['GET'])
def places(request):
    queryset = Thing.objects.filter(category=3)
    serializer = ThingSerializer(queryset,many=True,context={'request':request})
    
    return Response(serializer.data)

@api_view(['GET'])
def things_details(request,pk):
    # thing = Thing.objects.get(pk=pk)
    thing = get_object_or_404(Thing,pk=pk)

    serializer = ThingSerializer(thing,context={'request':request})
    
    return Response(serializer.data)

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    print(serializer.data)
    user = User.objects.create_user(**serializer.data)
    return Response(status=status.HTTP_201_CREATED)




@api_view(['POST'])
def log_in(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = authenticate(request, username=serializer.data['username'], password=serializer.validated_data['password'])

    if user is not None:
        login(request,user)
        return Response(serializer.data,status=status.HTTP_200_OK)
    else:

        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me(request):
    user=request.user
    # if user.is_anonymous:
    #     return Response(status=status.HTTP_401_UNAUTHORIZED)
    serializer = UserSerializer(user)
    return Response(serializer.data)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def log_out(request):
    logout(request)
    return Response(status=status.HTTP_200_OK)
