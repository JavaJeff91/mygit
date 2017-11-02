from rest_framework import serializers
from .models import Author,Book

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ['name','age','married','introduce',]

class BookSerializer(serializers.ModelSerializer):
    #author = serializers.ReadOnlyField(source='Author.name')
    class Meta:
        model = Book
        fields = ['name','info','type','status','count']
