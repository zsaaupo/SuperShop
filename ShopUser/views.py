from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from .serializers import CustomUserSerializer
from .models import CustomUser


class UserRegistrationAPIView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    
    def post(self, request, *args, **kwargs):
        result = {}
        try:
            data = request.data
            if 'name' not in data or data['name'] == '':
                result['massage'] = "name can not be null."
                result['error'] = "Name"
                return Response(result, status=HTTP_400_BAD_REQUEST)
            if 'email' not in data or data['email'] == '':
                result['massage'] = "Email can not be null."
                result['error'] = "Email"
                return Response(result, status=HTTP_400_BAD_REQUEST)
            if 'password' not in data or data['password'] == '':
                result['massage'] = "Password can not be null."
                result['error'] = "Password"
                return Response(result, status=HTTP_400_BAD_REQUEST)
            
            response = super().post(request, *args, **kwargs)
            if response.status_code == 201:
                user = self.get_serializer().Meta.model.objects.get(email=request.data.get('email'))
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=201)
            return response

        except Exception as ex:
            return Response(str(ex))
        return Response("True")

        


class UserLoginAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        result = {}
        try:
            data = request.data
            if 'email' not in data or data['email'] == '':
                result['message'] = "Email cannot be null."
                result['error'] = "Email"
                return Response(result, status=400)
            if 'password' not in data or data['password'] == '':
                result['message'] = "Password cannot be null."
                result['error'] = "Password"
                return Response(result, status=400)
            
            email = request.data.get('email')
            password = request.data.get('password')
            user = authenticate(request, email=email, password=password)
            
            if user is not None:
                login(request, user)
                token, created = Token.objects.get_or_create(user=user)
                
                return Response({'token': token.key}, status=200)
            
            return Response({'error': 'Invalid credentials'}, status=401)
        
        except Exception as ex:
            return Response(str(ex))