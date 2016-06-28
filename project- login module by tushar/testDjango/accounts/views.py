from django.shortcuts import render_to_response


# Create your views here.
from django.template import RequestContext


def home(request):
    return render_to_response('accounts/home.html',context_instance=RequestContext(request))
