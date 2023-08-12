from django.urls import path
from Koko_Krkr.views import *
from Koko_Krkr import views
from rest_framework import routers

handler404 = 'Koko_Krkr.views.custom_404'


urlpatterns =[
    path('',views.First_view, name='First-view'),
    path('cv/',CV_view.as_view(), name = 'cv-view'),
    path('friend/',views.BookVieww.as_view(
        {
            'get':'list',
            'post':'create',
        }
    )),
    path('friend/<int:pk>/',views.BookVieww.as_view(
        {
            'get':'retrieve',
            'post':'update',
            'patch':'partial_retrieve',
            'delete':'destroy',
        }
    )),

]