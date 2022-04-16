from django.urls import path

from hello1 import views

urlpatterns=[
            path('',views.index,name='index'),
            path('Email',views.Email,name='Email')
]
