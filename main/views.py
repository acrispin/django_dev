# from django.shortcuts import render

# # Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, _id):
    return HttpResponse("You're looking at question %s." % _id)

def results(request, qid):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % qid)

def vote(request, id):
    return HttpResponse("You're voting on question %s." % id)