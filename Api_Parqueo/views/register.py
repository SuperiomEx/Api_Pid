from rest_framework import generics, status
from rest_framework.response import Response
from ..utils.serializers import UserRegistrationSerializer

class UserRegistrationAPIView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        token_data = serializer.get_token(user)
        response_data = {
            'user': {
                'email': user.email,
                'nombre': user.nombre
            },
            'tokens': token_data
        }
        return Response(response_data, status=status.HTTP_201_CREATED)