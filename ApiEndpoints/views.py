from django.contrib.auth.models import User
from rest_framework import authentication, permissions, status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .permissions import IsLoggedIn
from .serializers import *


class PostView(APIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsLoggedIn]

    def get(self, request, *args, **kwargs):
        post_data = Post.objects.all()
        serializer = PostSerializer(post_data, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response({"errors": serializer.errors}, status=400)

    def put(self, request, pk, format=None):
        instance_data = Post.objects.get(id=pk)
        serializer = PostSerializer(instance_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(instance_data, data=request.data)

    def patch(self, request, pk, format=None):
        instance_data = Post.objects.get(id=pk)
        serializer = PostSerializer(instance_data, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(instance_data, data=request.data)

    def delete(self, request, pk, format=None):
        instance_data = Post.objects.get(id=pk)
        instance_data.delete()
        return Response({"msg": "Message Deleted"})


class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    permission_classes = [IsAuthenticated]
