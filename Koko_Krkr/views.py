from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .models import *
from .serializer import *

from django.views.generic.base import TemplateView 

from rest_framework.decorators import api_view,permission_classes,throttle_classes
from rest_framework.throttling import AnonRateThrottle
from rest_framework.response import Response
from rest_framework import status, viewsets, generics
from rest_framework.status import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser


def First_view(request):
    return HttpResponse('What everybody knows')


class CV_view(TemplateView):    
    template_name = 'cv.html'


def custom_404(request, exception):
    return render(request, '404.html', status=404)
