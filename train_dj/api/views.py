from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from django.shortcuts import render

from .serializer import UserSerializer
from .models import User, Question, Result


# Create your views here.
@api_view(['GET'])
def apiOverview(request):
  basicApi_urls = {
    'List':'/user-list/',
    'Detail':'/user-detail/<str:pk>',
    'Create':'/user-create/',
    'Update':'/user-update/<str:pk>',
    'Delete':'/user-delete/<str:pk>',
  }
  return Response(basicApi_urls)

@api_view(['GET'])
def userList(request):
  w = User.objects.all()
  serializer = UserSerializer(w, many=True)  # many=true returns more objects
  return Response (serializer.data)

@api_view(['GET'])
def userDetail(request, pk):
  w = User.objects.get(id=pk)
  serializer = UserSerializer(w, many=False) # many=false returns one object
  return Response (serializer.data)

@api_view(['POST'])
def userCreate(request):
  serializer = UserSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response (serializer.errors)

@api_view(['POST'])
def userUpdate(request, pk):
  w = User.objects.get(id=pk)
  serializer = UserSerializer(instance=w, data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response (serializer.errors)

@api_view(['DELETE'])
def userDelete(request, pk):
  w = User.objects.get(id=pk)
  w.delete()
  return Response ("Deleted")