from rest_framework import serializers
from .models import reader, book
from rest_framework.renderers import JSONRenderer
from rest_framework.serializers import ModelSerializer


class readerSr(serializers.Serializer):
    full_name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    number = serializers.IntegerField()
    email = serializers.EmailField()
    address = serializers.CharField(max_length=255)
    book_id = serializers.IntegerField()


    def create(self, validated_data):
        return reader.objects.create(**validated_data)
    

    def update(self, instance, validated_data):
        instance.full_name = validated_data.get("full_name", instance.full_name)
        instance.age = validated_data.get("age", instance.age)
        instance.number = validated_data.get("number", instance.number)
        instance.email = validated_data.get("email", instance.email)
        instance.address = validated_data.get("address", instance.address)
        instance.book_id = validated_data.get("book_id", instance.book_id)
        instance.save()
        return instance


class readerSrDel(serializers.ModelSerializer):
    class Meta:
        model = reader
        fields = "__all__"


class bookSrDel(serializers.ModelSerializer):
    class Meta:
        model = book
        fields = "__all__"

