from django.urls import path

from .views import show_score

urlpatterns = [
    path('student-score/',show_score,name="score")
]