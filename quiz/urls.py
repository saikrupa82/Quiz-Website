from .views import *
from django.urls import path,re_path
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('CreateQuiz/<slug>',PreviewQuizCreating,name="PreviewQuizCreating"),
    path('OrginalQuiz/<slug>',PreviewQuizWriting,name="PreviewQuizWriting"),
    path('EditQuiz/<slug>',EditQuiz ,name='EditQuiz'),
    path('EditQuizRedirect/<slug>',EditQuiz1 ,name='editquiz1'),
    path('EndQuiz',EndQuiz ,name='Endquiz'),
]