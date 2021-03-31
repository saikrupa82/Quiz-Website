from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.userLogin, name='userLogin'),
    path('studentDash/', views.student_index, name='studentDash'),
    path('teacherDash/', views.lecturer_index, name='teacherDash'),
]
