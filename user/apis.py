from django.shortcuts import render
from rest_framework import views , response , exceptions , permissions
from .serializer import *
from rest_framework import status
# Create your views here.

class RegisterApi(views.APIView):
    def post(self , request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        
        print(data)
        return response.Response(data , status=status.HTTP_200_OK)
