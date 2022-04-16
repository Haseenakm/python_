from django.urls import path

from saloonapp import views

urlpatterns = [
    path(" ", views.home, name='home'),
    path("signin",views.signin,name='signin'),
    path("register",views.register,name='register'),
    path('Admin_Home',views.Admin_Home,name='Admin_Home'),
    path('User_Home', views.User_Home, name='User_Home')
]