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

class BookVieww(viewsets.ViewSet):
     def list(self, request):
        friendo = Friends.objects.all()
        serializersfriend = friendserializer(friendo,many = True)
        return Response({"Message":serializersfriend.data},status.HTTP_200_OK)
     def create(self, request):
        serializersfriend = friendserializer(data=request.data)
        serializersfriend.is_valid(raise_exception=True)
        serializersfriend.save()
        return Response({"Message":serializersfriend.data},status.HTTP_201_CREATED)
     def update(self, request,pk = None):
        return Response({"Message":'update a book'},status.HTTP_200_OK)
     def retrieve(self, request,pk = None):
        friendo = Friends.objects.get(pk = pk)
        serializersfriend = friendserializer(friendo)
        return Response({"Message":serializersfriend.data},status.HTTP_200_OK)
     def partial_retrieve(self, request,pk = None):
        return Response({"Message":'partially '},status.HTTP_200_OK)
     def destroy(self, request,pk = None):
        friendo = Friends.objects.get(pk = pk)
        friendo.delete()
        return Response({"Message":f'Friend with id {pk} is destroy'},status.HTTP_200_OK)


def custom_404(request, exception):
    return render(request, '404.html', status=404)
