from .models import Libro, Autor, File
from .serializers import LibroSerializer, AutorSerializer, FileSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import logging
logger = logging.getLogger(__name__)

## http://www.django-rest-framework.org/tutorial/3-class-based-views/

class FileList(APIView):
    """
    List all files, or create a new file.
    """
    def get(self, request, format=None):
        files = File.objects.all()
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileDetail(APIView):
    """
    Retrieve, update or delete a file instance.
    """
    def get_object(self, pk):
        try:
            return File.objects.get(pk=pk)
        except File.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        item = self.get_object(pk)
        serializer = FileSerializer(item)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        item = self.get_object(pk)
        serializer = FileSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        