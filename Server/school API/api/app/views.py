from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ContactSerializer
from .serializers import RegisterSerializer
from .serializers import RegisterloginSerializer
# from .serializers import BookingSerializer
from .serializers import BookSerializer
from rest_framework.permissions import AllowAny
from .models import contact
from .models import register
# from .models import Booking
from .models import Book


@api_view(['POST'])
def cont(request):
    if request.method=='POST':
        serializer=ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({'msg':'saved successfully','data':serializer.data})
        
        
@api_view(['POST'])
def reg(request):
    if request.method=='POST':
        serializer=RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'saved successfully','data':serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(['POST'])
# def book(request):
#     if request.method=='POST':
#         serializer=BookingSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'saved successfully','data':serializer.data})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def book(request):
    if request.method=='POST':
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'saved successfully','data':serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')
        user = register.objects.filter(email=email, password=password)
        print(user)
        if user:

            return Response({'message':"login successfull"})
        else:
           
            return Response({'error': 'Invalid credentials'})
        



    
@api_view(['GET'])
def one(request):
# def display(request,id):
    if request.method=='GET':
        data=contact.objects.all()
        serializer=ContactSerializer(data,many=True,context={'request':request})
        return Response(serializer.data)
    
@api_view(['GET'])
def display(request) :
    if request.method=='GET':
        data=register.objects.all()
        serializer=RegisterSerializer(data,many=True,context={'request':request})
        return Response(serializer.data)
    
@api_view(['GET'])
def two(request):
# def display(request,id):
    if request.method=='GET':
        data=Book.objects.all()
        serializer=BookSerializer(data,many=True,context={'request':request})
        return Response(serializer.data)
    
