from django.shortcuts import render, get_object_or_404, redirect
from .models import Quiz, Question, QuizAttempt
from django.contrib.auth.decorators import login_required
from courses.models import Course
from .forms import QuizForm

@login_required
def attempt_quiz(request, id):
    quiz = get_object_or_404(Quiz, id=id)
    questions = Question.objects.filter(quiz=quiz)

    if request.method == "POST":
        score = 0

        for question in questions:
            selected = request.POST.get(str(question.id))
            if selected == question.correct_answer:
                score += 1

        QuizAttempt.objects.create(
            quiz=quiz,
            student=request.user,
            score=score
        )

        return render(request, "quizzes/quiz_result.html", {
            "score": score,
            "total": questions.count()
        })

    return render(request, "quizzes/attempt_quiz.html", {
        "quiz": quiz,
        "questions": questions
    })

def create_quiz(request, course_id):
    course = Course.objects.get(id=course_id)

    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.course = course
            quiz.save()
            return redirect('dashboard')
    else:
        form = QuizForm()

    return render(request, 'quizzes/create_quiz.html', {'form': form, 'course': course})





