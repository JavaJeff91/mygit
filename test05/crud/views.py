from django.shortcuts import render,render_to_response
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import AuthorSerializer,BookSerializer
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from . import models
from rest_framework import exceptions,status


def test(self):
    return render_to_response('successed.html',{'param':''})


# Create your views here.
class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    permission_classes = [IsOwnerOrReadOnly]
    # TODO 还差一个自定义权限

    def get_queryset(self):
        queryset = models.Author.objects.all()
        return queryset
    
    def create(self, request):

        context = dict(request=request)
        serializer = AuthorSerializer(data=request.data,context=context)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self, request):

        context = dict(request=request)
        serializer = AuthorSerializer(data=request.data,context=context)
        if serializer.is_valid():
            serializer.update()
            return Response(data=serializer.data,status=status.HTTP_202_ACCEPTED)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request):
        context = dict(request=request)
        serializer = AuthorSerializer(data=request.data, context=context)
        if serializer.is_valid():
            author = models.Author.objects.filter(id=request.data['id'])
            author.delete()
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    #permission_classes = permissions.IsAuthenticatedOrReadOnly

    def get_queryset(self):

        queryset = models.Book.objects.all()
        return queryset

    def create(self, request):

        context = dict(request=request)
        serializer = BookSerializer(data=request.data, context=context)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)



