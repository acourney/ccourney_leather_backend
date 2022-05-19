from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from rest_framework import generics, permissions  
from .models import Item
from .serializers import ItemSerializer
# Create your views here.

class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer