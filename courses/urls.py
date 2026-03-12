from django.urls import path
from .views import create_course
from . import views
from accounts.views import upload_lesson

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('create/', create_course, name='create_course'),
    path('<int:course_id>/enroll/', views.enroll_course, name='enroll_course'),
    path('upload-lesson/<int:course_id>/', upload_lesson, name='upload_lesson'),
]