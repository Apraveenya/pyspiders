from django.urls import path
from pythonfullstack.views import *
appname='pythonfullstack'
urlpatterns=[
    path('python/',python,name='python'),
]