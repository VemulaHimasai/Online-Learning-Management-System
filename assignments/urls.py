from django.urls import path
from . import views

urlpatterns = [
    path('submit/<int:id>/', views.submit_assignment, name='submit_assignment'),
    path('submissions/<int:assignment_id>/', views.view_submissions, name='view_submissions'),
]