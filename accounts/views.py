from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from courses.models import Course, Enrollment, Lesson
from courses.forms import LessonForm
from quizzes.models import Quiz, QuizAttempt
from assignments.models import Assignment


# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            context = {'error': 'Invalid username or password'}
            return render(request, 'accounts/login.html', context)
    return render(request, 'accounts/login.html')

@login_required
def dashboard(request):

    if request.user.role == 'student':
        courses = Course.objects.all()

        enrolled_courses =[]

        for course in courses:
            is_enrolled = Enrollment.objects.filter(student=request.user, course=course).exists()
            course.is_enrolled = is_enrolled

            if is_enrolled:
                enrolled_courses.append(course)
            
        quizzes = Quiz.objects.filter(course__in=enrolled_courses)
        attempts = QuizAttempt.objects.filter(user=request.user)
        assignments = Assignment.objects.filter(course__in=enrolled_courses)
        return render(request, 'accounts/student_dashboard.html', {
            'courses': enrolled_courses,
            'quizzes': quizzes,
            'attempts': attempts,
            'assignments': assignments
        })
    else:
        courses = Course.objects.filter(teacher=request.user)
        assignments = Assignment.objects.filter(course__in=courses)
        return render(request, 'accounts/teacher_dashboard.html', {'courses': courses, 'assignments': assignments})
@login_required
def upload_lesson(request, course_id):
    if request.user.role != 'teacher':
        return redirect('dashboard')

    course = Course.objects.get(id=course_id)

    if request.method == 'POST':
        form = LessonForm(request.POST, request.FILES)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.course = course
            lesson.save()
            return redirect('dashboard')
    else:
        form = LessonForm()

    return render(request, 'accounts/upload_lesson.html', {'form': form, 'course': course})
    
@login_required
def student_dashboard(request):
    enrolled_courses = request.user.enrolled_courses.all()
    all_courses = Course.objects.all()


    for course in enrolled_courses:
        course.lessons = Lesson.objects.filter(course=course)
    
    quizzes = Quiz.objects.filter(course__in=enrolled_courses)

    attempts = QuizAttempt.objects.filter(user=request.user)

    assignments = Assignment.objects.filter(course__in=enrolled_courses)

    return render(request, 'accounts/student_dashboard.html',{
        'courses':enrolled_courses,
        'all_courses':all_courses,
        'quizzes':quizzes,
        'attempts':attempts,
        'assignments':assignments
    })

@login_required
def teacher_dashboard(request):
    print("Logged in user:", request.user)

    courses = Course.objects.filter(teacher=request.user)
    assignments = Assignment.objects.filter(course__in=courses)
    return render(request, 'accounts/teacher_dashboard.html', {'courses': courses, 'assignments': assignments})

@login_required
def create_assignment(request, course_id):
    if request.user.role != 'teacher':
        return redirect('dashboard')
    
    return render(request, 'accounts/create_assignment.html', {'course_id':course_id})
