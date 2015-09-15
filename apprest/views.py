from django.shortcuts import render
from django.http import HttpResponse
from django.core.signals import request_started
from django.core.signals import request_finished
from django.db import connection

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Libro, Autor, File
from .serializers import LibroSerializer, AutorSerializer, FileSerializer

import time
import simplejson

import logging
logger = logging.getLogger(__name__)

## https://realpython.com/blog/python/django-rest-framework-quick-start/
## http://www.dabapps.com/blog/api-performance-profiling-django-rest-framework/

def started(sender, **kwargs):    
    global start_time
    start_time = time.time()

def finished(sender, **kwargs):
    total_time = time.time() - start_time
    print ("Database lookup               | %.6fs" % db_time)
    print ("Serialization                 | %.6fs" % serializer_time)
    print ("Django request/response       | %.6fs" % total_time)

request_started.connect(started)
request_finished.connect(finished)


def home(request):    
    return render(request, 'rest/index.html')


@api_view(['GET', 'POST'])
def file_collection(request):
    global serializer_time
    global db_time

    if request.method == 'GET':

        db_start = time.time()
        files = File.objects.all()
        db_time = time.time() - db_start

        serializer_start = time.time()
        serializer = FileSerializer(files, many=True)
        serializer_time = time.time() - serializer_start

        return Response(serializer.data)

    elif request.method == 'POST':
        logger.debug(request.data)
        # return Response(request.data, status=status.HTTP_201_CREATED)
        return Response(request.data)



@api_view(['GET', 'DELETE'])
def file_element(request, pk):
    code = request.GET.get('code', "")
    active = request.GET.get('active', "")
    logger.debug("code: {0}, active: {1}".format(code, active))

    try:
        _file = File.objects.get(pk=pk)
    except File.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = FileSerializer(_file)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def file_collection2(request):
    global serializer_time
    global db_time

    db_start = time.time()
    data = File.objects.values('id', 'pathfile')
    db_time = time.time() - db_start

    serializer_time = 0

    return Response(data)


@api_view(['GET'])
def file_collection3(request):
    global serializer_time
    global db_time

    db_start = time.time()
    items = File.objects.all()
    db_time = time.time() - db_start

    serializer_start = time.time()
    serializer = FileSerializer(items, many=True)
    serializer_time = time.time() - serializer_start

    #return Response(serializer.data)
    return HttpResponse(simplejson.dumps(serializer.data), 
                        content_type='application/json; charset=utf-8')

@api_view(['GET'])
def file_collection4(request):
    global serializer_time
    global db_time

    db_start = time.time()
    items = File.objects.raw('SELECT id, pathfile FROM apprest_file')
    db_time = time.time() - db_start

    serializer_start = time.time()
    serializer = FileSerializer(items, many=True)
    serializer_time = time.time() - serializer_start

    #return Response(serializer.data)
    return HttpResponse(simplejson.dumps(serializer.data), 
                        content_type='application/json; charset=utf-8')

@api_view(['GET'])
def file_collection5(request):
    global serializer_time 
    global db_time

    db_start1 = time.time()
    with connection.cursor() as cursor:
        cursor.execute('SELECT id, pathfile FROM apprest_file')
        data = dictfetchall(cursor)
    db_time1 = time.time() - db_start1

    serializer_start1 = time.time()
    json = simplejson.dumps(data)
    serializer_time1 = time.time() - serializer_start1

    db_time = db_time1
    serializer_time = serializer_time1

    logger.debug("Database lookup               | %.6fs" % db_time1)
    logger.debug("Serialization                 | %.6fs" % serializer_time1)

    return HttpResponse(json, content_type='application/json; charset=utf-8')    

@api_view(['GET'])
def file_collection6(request):
    global serializer_time
    global db_time

    db_start = time.time()
    with connection.cursor() as cursor:
        cursor.execute('SELECT id, pathfile FROM apprest_file')
        json = getDictJsonFromCursor(cursor)
    db_time = time.time() - db_start

    serializer_time = 0

    return HttpResponse(json, content_type='application/json; charset=utf-8')

@api_view(['GET'])
def file_collection7(request):
    global serializer_time
    global db_time

    db_start = time.time()
    with connection.cursor() as cursor:
        _id = request.GET.get('id', '0')
        cursor.execute('SELECT id, pathfile FROM apprest_file where id = %s', [int(_id)])
        print cursor.query
        json = getDictJsonFromCursor2(cursor)
    db_time = time.time() - db_start

    serializer_time = 0

    return HttpResponse(json, content_type='application/json; charset=utf-8')

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

def getDictJsonFromCursor(cursor):
    rows = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    results = [dict(zip(columns,row)) for row in rows]
    return simplejson.dumps(results)

def getDictJsonFromCursor2(cursor):
    rows = cursor.fetchall()
    if len(rows) == 1:
        columns = [column[0] for column in cursor.description]
        rs = [dict(zip(columns,row)) for row in rows][0]
    else:
        rs = {}
    return simplejson.dumps(rs)
