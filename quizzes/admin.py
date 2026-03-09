from django.contrib import admin
from .models import Quiz , Question, QuizAttempt


# Register your models here.

admin.site.register(Quiz)
admin.site.register(Question)
# admin.site.register(QuizAttempt)

@admin.register(QuizAttempt)
class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ['user', 'quiz', 'score', 'total', 'attempted_at']

