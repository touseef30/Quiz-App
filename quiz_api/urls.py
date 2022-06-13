from django.urls import path
from .views import *
urlpatterns = [
    path('quiz/', QuizView.as_view()),
    path('result/', ResultView.as_view())
]
