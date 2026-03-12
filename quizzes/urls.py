from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz_dashboard, name='quiz_dashboard'),
    path('list/', views.quiz_list, name='quiz_list'),
    path('attempt/<int:id>/', views.attempt_quiz, name='attempt_quiz'),
    path('create/<int:course_id>/', views.create_quiz, name='create_quiz'),
]