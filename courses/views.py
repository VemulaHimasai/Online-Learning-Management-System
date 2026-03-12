from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Course , Enrollment
from .forms import CourseForm

# Create your views here.

@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

@login_required
def create_course(request):
    if request.user.role != 'teacher':
        return redirect('dashboard')
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.teacher = request.user
            course.save()
            return redirect('dashboard')
    else:
        form = CourseForm()
    return render(request, 'courses/create_course.html', {'form':form})

@login_required
def enroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.user.role != 'student':
        return redirect('dashboard')
    
    Enrollment.objects.get_or_create(student=request.user, course=course)

    return redirect('dashboard')

