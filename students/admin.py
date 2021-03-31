from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import *

# @admin.register(Test)
# class TestAdmin(ImportExportModelAdmin):
#     list_display=('test',
#     'rollno',
#     'totalscore',
#     'securedscore',
#     'correct_answer',
#     'wrong_answer',
# )
@admin.register(Student_Details)
class Student_DetailsAdmin(ImportExportModelAdmin):
    list_display=(
        'Rollno',
        'Name',
    )
@admin.register(LeaderBoard)
class LeaderBoardAdmin(ImportExportModelAdmin):
    list_display=('rollno','test' ,

)
@admin.register(Label)
class TestBoardAdmin(ImportExportModelAdmin):
    list_display=(
    'TestName',
)

@admin.register(Session_Details)
class Session_DetailsAdmin(ImportExportModelAdmin):
    list_display=(
    'date','Session_Name'
)

