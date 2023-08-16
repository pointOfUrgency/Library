from django.shortcuts import render
from rest_framework.response import Response
from .serializers import readerSr
from rest_framework.views import APIView
from .models import reader


class libraryAPI(APIView):
    def get(self, request):
        lst = reader.objects.all()
        return Response({"readers:": readerSr(lst, many=True).data})
