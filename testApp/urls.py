from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('register', views.register_board),
    path('login', views.login),
    path('signup', views.sign_up)


]