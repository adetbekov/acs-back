from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from django.contrib.auth.models import User
from .serializers import UserSerializer

class UserListAPIView(APIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer()

class CurrentUserView(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

# class UserView(APIView):
#     def get(self):
#     	pk = self.kwargs['pk']
#         serializer = UserSerializer(request.user)
#         return Response(serializer.data)

