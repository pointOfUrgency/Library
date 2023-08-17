from django.shortcuts import render
from rest_framework.response import Response
from .serializers import readerSr
from rest_framework.views import APIView
from .models import reader


class libraryAPI(APIView):
    def get(self, request):
        lst = reader.objects.all()
        return Response({"readers:": readerSr(lst, many=True).data})
    

    def post(self, request):
        serializer = readerSr(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"post:": serializer.data})
    

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)

        if not pk:
            return Response({"error": "method PUT not allowed"})
        
        try:
            instance = reader.objects.get(pk=pk)
        except:
            return Response({"error": "this oject does not exist"})
        
        serializer = readerSr(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"post": serializer.data})
