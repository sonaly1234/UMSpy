from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from .models import User
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser


# Create your views here.

class UserAPIView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        userdetails = User.objects.all()
        serializer = UserSerializer(userdetails, many=True)
        return Response(serializer.data)
    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class UserDetailAPIView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist as err:
            return Response({"error": "Not Found"})

    def get(self, request, id=None):
        instance = self.get_object(id)
        serializer = UserSerializer(instance)
        return Response(serializer.data)

    def put(self, request, id=None):
        data = request.data
        instance = self.get_object(id)
        serializer = UserSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id=None):
        instance = self.get_object(id)
        instance.delete()
        return Response("Deleted")





