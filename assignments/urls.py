from django.urls import path
from . import views

urlpatterns = [
     path('', views.assignment_list, name='assignment_list'),
    path('submit/<int:id>/', views.submit_assignment, name='submit_assignment'),
    path('submissions/<int:assignment_id>/', views.view_submissions, name='view_submissions'),
    path('create-assignment/<int:course_id>/', views.create_assignment, name='create_assignment'),
]