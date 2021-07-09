from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from manager.models import Comment, LikeCommentUser, Book, LikeBookUser as RateBookUser


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class LKUSerializer(ModelSerializer):
    class Meta:
        model = LikeCommentUser
        fields = '__all__'


class BookSerializer(ModelSerializer):
    date = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Book
        fields = ['title', 'description', 'date']


class AddRateSerializer(ModelSerializer):
    class Meta:
        model = RateBookUser
        fields = '__all__'

