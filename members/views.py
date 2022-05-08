from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from .models import User


@api_view(["POST"])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

@api_view(["GET"])
def get_user(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data) 

@api_view(["PUT"])
# @permission_classes([IsAuthenticated])
def update_user(request, pk):
    data = request.data

    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, data=request.POST)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
