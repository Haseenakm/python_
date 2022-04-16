from django.urls import path
from saloon import views
urlpatterns=[
    path('',views.home,name='home'),
    path('signin',views.signin,name='signin')
]