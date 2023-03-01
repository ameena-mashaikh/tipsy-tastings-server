from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.db import IntegrityError
from rest_framework import status
from tipsytastingapi.models import Mixologist


@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    '''Handles the authentication of a mixologist

    Method arguments:
      request -- The full HTTP request object
    '''
    username = request.data['username']
    password = request.data['password']

    # Use the built-in authenticate method to verify
    # authenticate returns the user object or None if no user is found
    authenticated_user = authenticate(username=username, password=password)

    # If authentication was successful, respond with their token
    if authenticated_user is not None:
        token = Token.objects.get(user=authenticated_user)
        data = {
            'valid': True,
            'token': token.key
        }
        print(token.key)
        return Response(data)
    else:
        # Bad login details were provided. So we can't log the user in.
        data = { 'valid': False }
        return Response(data)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''
    print(request.data)
    try:
        new_user = User.objects.create_user(
            username=request.data.get('username'),
            password=request.data.get('password'),
            first_name=request.data.get('first_name'),
            last_name=request.data.get('last_name')
        )
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    try:
        mixologist = Mixologist.objects.create(
            user=new_user
            # bio=request.data.get('bio'),
            # image = request.data.get('image')
        )
    except Exception as e:
        new_user.delete()
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    token = Token.objects.create(user=mixologist.user)
    data = { 'token': token.key }
    return Response(data)


#   "bio": "I barely drink, but sweet cocktails are my favorite!",
#         "image": "https://wallpapercave.com/uwp/uwp1174000.png"
























# def register_user(request):
#     '''Handles the creation of a new mixologist for authentication

#     Method arguments:
#       request -- The full HTTP request object
#     '''

#     # Create a new user by invoking the `create_user` helper method
#     # on Django's built-in User model
#     new_user = User.objects.create_user(
#         username = request.data["username", None],
#         password = request.data['password', None],
#         first_name = request.data['first_name', None],
#         last_name = request.data['last_name', None]
#     )

#     # Now save the extra info in the tipsytastingapi Mixologist table
#     mixologist = Mixologist.objects.create(
#         bio=request.data['bio'],
#         user=new_user
#         #image = request.data['image']
#     )

#     # Use the REST Framework's token generator on the new user account
#     token = Token.objects.create(user=mixologist.user)
#     # Return the token to the client
#     data = { 'token': token.key }
#     return Response(data)
