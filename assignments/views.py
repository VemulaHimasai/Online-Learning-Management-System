from django.shortcuts import render, redirect, get_object_or_404
from .models import Assignment, Submission
from .forms import SubmissionForm

# Create your views here.

def submit_assignment(request, id):
    assignment = get_object_or_404(Assignment, id=id)

    existing_submission = Submission.objects.filter(assignment = assignment, student = request.user).first()

    if existing_submission:
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            submission = form.save(commit = False)
            submission.assignment = assignment
            submission.student = request.user
            submission.save()
            return redirect('dashboard')
    else:
        form = SubmissionForm()
    return render(request, 'assignments/submit_assignment.html',{'form': form, 'assignment': assignment})

def view_submissions(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    submissions = Submission.objects.filter(assignment = assignment)
    return render(request, 'assignments/view_submissions.html', {'assignment': assignment, 'submissions': submissions})