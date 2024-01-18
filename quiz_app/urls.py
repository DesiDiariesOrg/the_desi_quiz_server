from django.urls import path
from .views import QuestionListAPIView

urlpatterns = [
    path('api/questions/', QuestionListAPIView.as_view(), name='question-list'),
]
