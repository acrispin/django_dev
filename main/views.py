from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

import logging
logger = logging.getLogger(__name__)

def index0(request):
    return HttpResponse("Hello, world. You're at the polls index.")

#@login_required # se debe crear el path /accounts/login/
def index(request):
    logger.debug('home page ...........')
    context = {'username': "Administrador"}
    request.session['username'] = "Administrator"
    return render(request, 'main/index.html', context)

def detail(request, _id):
    return HttpResponse("You're looking at question %s." % _id)

def results(request, qid):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % qid)

def vote(request, id):
    return HttpResponse("You're voting on question %s." % id)