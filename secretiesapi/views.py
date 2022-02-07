from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Post
from .serializers import PostSerializer




@api_view(['GET','POST'])
def getPost(request):
    if request.method == "GET":
        post = Post.objects.last()
        serializer = PostSerializer(post, many=False)
        return Response(serializer.data)
    if request.method == "POST":
        data = request.data
        post =  Post.objects.create(
            content = data['content']
            )
        serializer = PostSerializer(post, many=False)
        return Response(serializer.data)



        
