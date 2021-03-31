from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

@admin.register(Quiz)
class QuizAdmin(ImportExportModelAdmin):
    list_display=(
        'Session_Name',
        'NameOfTest',
        'Question',
        'Answer',
    )
@admin.register(QuizList)
class QuizListAdmin(ImportExportModelAdmin):
    list_display=(
        'Session_Name',
        'NameOfTest',
        'NumberOfQuestions',
    )