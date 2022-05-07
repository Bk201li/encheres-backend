from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from .models import User
import jwt, datetime


@api_view(["POST"])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(["POST"])
def login_user(request): 
    email = request.data['email']
    password = request.data['password']
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        raise AuthenticationFailed('User not found!')
    
    if not user.check_password(password):
        raise AuthenticationFailed('Incorrect password!')

    payload = {
        'id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        'iat': datetime.datetime.utcnow()
    }

    token = jwt.encode(payload, 'secret', algorithm='HS256')
    
    response = Response()

    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {
        'jwt': token
    }

    return response


@api_view(["POST"])
def logout_user(request):
    response = Response()
    response.delete_cookie('jwt')
    response.data = {
        'message': 'User logged out!'
    }

    return response


@api_view(["GET"])
def get_user(request):
    token = request.COOKIES.get('jwt')

    if not token:
        raise AuthenticationFailed('User not logged in!')
    
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('User not logged in!')

    user = User.objects.get(id=payload['id'])
    serializer = UserSerializer(user)

    return Response(serializer.data)   
