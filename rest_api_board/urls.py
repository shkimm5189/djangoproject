from django.urls import path
from rest_api_board import views

urlpatterns = [
    path('', views.BoardView.as_view()),
    path('<int:idx>', views.BoardView.as_view())
]