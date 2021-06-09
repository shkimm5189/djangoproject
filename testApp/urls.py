from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('register', views.register_board),

]