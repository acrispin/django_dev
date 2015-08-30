#from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext

from .models import Choice, Question

import logging
logger = logging.getLogger(__name__)

def homepage(request):
    """
    Shows the homepage with a welcome message that is translated in the
    user's language.
    """
    message = ugettext('Welcome to our site!')
    return render(request, 'polls/homepage.html', {'message': message})

#@login_required # se debe crear el path /accounts/login/
def index(request):

    ## test de logger
    logger.debug('test de debug...........')
    # logger.info('test de info...........')
    # logger.warning('test de warn...........')
    # logger.error('test de error...........')
    # logger.critical('test de critical...........')

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context) # busca en el file: /polls/templates/index.html

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question': question})
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))