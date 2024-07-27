from django.shortcuts import render
from rest_framework import viewsets
from .models import Post, Comentario
from .serializers import PostSerializer, ComentarioSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
