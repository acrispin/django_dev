from easy_pdf.views import PDFTemplateView
from easy_pdf.rendering import render_to_pdf, render_to_pdf_response
from django.http import HttpResponse
from rest_framework.decorators import api_view
import simplejson
import requests

from polls.models import Choice

import logging
logger = logging.getLogger(__name__)

class HelloPDFView(PDFTemplateView):
    template_name = "main/hello.html"

    def get_context_data(self, **kwargs):
        return super(HelloPDFView, self).get_context_data(
            pagesize="A4",
            title="Hi there!",
            **kwargs
        )


class HelloPDFView2(PDFTemplateView):
    query_results = Choice.objects.all()
    # print "DEBUG : ", query_results
    # logger.debug(query_results)
    template_name = "main/hello2.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        print "DEBUG : ", self.query_results
        logger.debug(self.query_results)
        context["query_results"] = self.query_results

        return self.render_to_response(context)        


class HelloPDFView3(PDFTemplateView):
    query_results = Choice.objects.all()
    template_name = "main/hello2.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context["query_results"] = self.query_results
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="filename.pdf"'
        bts = render_to_pdf(self.template_name, context)    
        # logger.debug(bts)
        # logger.debug(str(bts))
        response.write(bts)
        return response


class HelloPDFView4(PDFTemplateView):
    query_results = Choice.objects.all()
    template_name = "main/hello2.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context["query_results"] = self.query_results
        cod = request.GET.get('cod', '')
        logger.debug("cod: " + cod)
        bts = render_to_pdf(self.template_name, context)    
        # rs = { "bts": str(bts.decode('utf-8'))}
        #rs = { "bts": str(bts)}

        # return HttpResponse(str(bts), 
        #                 content_type='application/pdf; charset=utf-8')

        # return HttpResponse(bts, 
        #                 content_type='application/text')

        return HttpResponse(bts, 
                        content_type='application/pdf')

# import base64

@api_view(['GET','POST'])
def hello_pdf_5(request):
    query_results = Choice.objects.all()
    template_name = "main/hello2.html"
    context = {}
    context["query_results"] = query_results
    cod = request.GET.get('cod', '')
    logger.debug("cod: " + cod)
    # bts = render_to_pdf(template_name, context)
    # logger.debug(type(bts))
    # rs = base64.b64encode(bts)
    # return HttpResponse(bts, content_type='application/pdf; charset=utf-8')
    # return HttpResponse(bts, content_type='application/x-www-form-urlencoded; charset=UTF-8')
    return render_to_pdf_response(request, template_name, context)


@api_view(['GET','POST'])
def hello_pdf_6(request):
    urlPdf = request.build_absolute_uri().replace("/pdf6", "/pdf4")
    logger.debug(urlPdf)
    r = requests.get(urlPdf)
    bts = r.text

    if request.method == 'GET':
        cod = request.GET.get('cod', '')
        logger.debug("cod: " + cod)

    elif request.method == 'POST':
        logger.debug(request.data)

    return HttpResponse(bts, content_type='application/pdf; charset=utf-8')
