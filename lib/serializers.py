from rest_framework import serializers
from .models import reader
from rest_framework.renderers import JSONRenderer


# class Comment:
#     def __init__(self, email, content, created=None):
#         self.email = email
#         self.content = content
#         self.created = created or datetime.now()

# comment = Comment(email='leila@example.com', content='foo bar')


# class CommentSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     content = serializers.CharField(max_length=200)
#     created = serializers.DateTimeField()


# def sr():
#     serialize = CommentSerializer(comment)
#     json = JSONRenderer().render(serialize.data)
#     print(json)


# def dsr():

class readerSr(serializers.Serializer):
    full_name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    number = serializers.IntegerField()
    email = serializers.EmailField()
    address = serializers.CharField(max_length=255)
    book_id = serializers.IntegerField()


