from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


# Create your views here.
def index(request):
    context = {}
    template = loader.get_template('schooldata/index.html')
    return HttpResponse(template.render(context, request))


def canvas(request):
    context = {}
    # The template to be loaded as per gentelella.
    # All resource paths for gentelella end in .html.

    # Pick out the html file name from the url. And load that template.
    load_template = request.path.split('/')[-1]
    template = loader.get_template('schooldata/' + load_template)
    return HttpResponse(template.render(context, request))
