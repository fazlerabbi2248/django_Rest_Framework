from rest_framework import serializers
from apibasic.models import *
from django.contrib.auth.models import User

class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    date = serializers.DateTimeField()

    def create(self, validated_data):
        return Article.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.email = validated_data.get('email', instance.email)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance

class ArticleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id','title','author']

class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ['id', 'username']


class UserLoginSerializer(serializers.ModelSerializer):
  username = serializers.CharField(max_length=255)
  class Meta:
    model = User
    fields = ['username', 'password']


