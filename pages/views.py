# Create your views here.

from django.http import HttpResponse


def home_page(request):
    return HttpResponse("I am back...")