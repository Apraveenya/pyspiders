from django.urls import path
from mernfullstack.views import *
appname='mernfullstack'
urlpatterns=[
    path('mern/',mern,name='mern'),
]