from .views import *
from django.urls import path,re_path
from django.contrib.auth import views as auth_views
from quiz.urls import *
urlpatterns = [
    path('', Login ,name='login'),
    path('test',Testing,name="Testing"),
    path('DashBoard', DashBoard ,name='dashboard'),
    path('profile',Profile,name='profile'),
    re_path(r'^ProfileView/(?P<slug>[-\w]+)/$',ProfileView,name='ProfileView'),
    path('LeaderBoard',Table,name='leaderboard'),
    re_path(r'^score/(?P<slug>[-\w]+)/$',DailyScoreBoard,name='score'),
    re_path(r'^Student/(?P<slug>[-\w]+)/$',statofstudent,name='stats'),
]
