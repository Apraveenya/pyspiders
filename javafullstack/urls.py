from django.urls import path
from javafullstack.views import *
appname='javafullstack'
urlpatterns=[
    path('java/',java,name='java'),
]