from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import logging
logger = logging.getLogger(__name__)

## http://stackoverflow.com/questions/13603027/django-rest-framework-non-model-serializer

class CalcClass(object):

    def __init__(self, *args, **kw):
        # Initialize any variables you need from the input you get
        pass

    def do_work(self):
        # Do some calculations here
        # returns a tuple ((1,2,3, ), (4,5,6,))
        result = ((1,2,3, ), (4,5,6,)) # final result
        return result

    def getJson(self):
        rs = {'name':'Carlos','code':'00293','active':True}
        return rs


class RestApiView(APIView):

    def get(self, request, *args, **kw):
        # Process any get params that you may need
        # If you don't need to process get params,
        # you can skip this part
        get_arg1 = request.GET.get('arg1', "")
        get_arg2 = request.GET.get('arg2', "")
        code = request.GET.get('code', "")
        active = request.GET.get('active', "")

        logger.debug("get_arg1: {0}, get_arg2: {1}".format(get_arg1, get_arg2))
        logger.debug("code: {0}, active: {1}".format(code, active))
        logger.debug(args)
        logger.debug(kw)

        # Any URL parameters get passed in **kw
        myClass = CalcClass(get_arg1, get_arg2, *args, **kw)
        result = myClass.do_work()
        response = Response(result, status=status.HTTP_200_OK)
        return response

class RestApiViewJson(APIView):

    def get(self, request, *args, **kw):
        # Process any get params that you may need
        # If you don't need to process get params,
        # you can skip this part
        get_arg1 = request.GET.get('arg1', "")
        get_arg2 = request.GET.get('arg2', "")

        logger.debug("get_arg1: {0}, get_arg2: {1}".format(get_arg1, get_arg2))
        logger.debug(args)
        logger.debug(kw)

        # Any URL parameters get passed in **kw
        myClass = CalcClass(get_arg1, get_arg2, *args, **kw)
        result = myClass.getJson()
        response = Response(result, status=status.HTTP_200_OK)
        return response        