import cStringIO as StringIO
from xhtml2pdf import pisa
# import ho.pisa as pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from cgi import escape

from polls.models import Question

import logging
logger = logging.getLogger(__name__)


def render_to_pdf(template_src, context_dict):
    logger.debug('INICIO')
    template = get_template(template_src)
    logger.debug('GET TEMPLATE')
    context = Context(context_dict)
    logger.debug('GET CONTEXT')
    html  = template.render(context)
    logger.debug('GET HTML')
    result = StringIO.StringIO()
    logger.debug('GET RESULT')
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)
    logger.debug('FIN')
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))

def convert(request):
    logger.debug('obtencion de preguntas')
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    logger.debug('inicio de context')
    context = {'latest_question_list': latest_question_list}
    #return render(request, 'polls/index.html', context)
    return render_to_pdf('polls/index.html', context)