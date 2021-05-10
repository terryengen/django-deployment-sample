from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context_dict = {'text': "Hello world!", 'number': 100}
    return render(request, 'tempapp01/index.html', context = context_dict)

def other(request):
    return render(request, 'tempapp01/other.html')

def relative(request):
    return render(request, 'tempapp01/rel_url_templ.html')
