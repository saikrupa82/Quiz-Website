from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from tablib import Dataset
from .models import *
import pandas as pd
import re,csv
import json
from django.utils import timezone
from quiz.models import *
from quiz.views import *
from users.decorators import *
from .forms import CustomUserUpdateForm
from django.views.decorators.csrf import csrf_exempt
import csv
from django.contrib.auth import get_user_model


@unauthenticated_user
def Login(request):
    if request.method=="POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect("/DashBoard")
            
    return render(request,'login2.html')
@csrf_exempt
def DashBoard(request):
    if request.user.is_lecturer or request.user.is_superuser:
        session=Session_Details.objects.all().filter(QuizCreator=request.user.username)
        context={'session':session}

    if request.user.is_student or request.user.is_superuser:
        quiz=QuizList.objects.all()
        session=Session_Details.objects.all()
        context={'session':session,'quiz':quiz}

    if request.method =='POST' and request.POST.get('popup1')=='popup1':
        print('hello')
        # print(request,POSTS.is_valid())
        Session_Name=request.POST['SessionName']
        Branch=request.POST.getlist('Branch')
        Year=request.POST.getlist('Year')
        TypeOfExam=request.POST.get('TypeOfExam')
        NameOfTest=request.POST['NameOfTest']
        print(TypeOfExam,NameOfTest)
        # print(Session_Name,Branch,Year,Quiz,Labs)
        print(Year,Branch)
        b,y='',''
        for i in Branch:
            b=b+i+'@'
        for j in Year:
            y=y+j+'@'
        print(b[:-1],y[:-1])
        r=''
        if TypeOfExam=="Quiz":
            r="Q"
        else:
            r="L"

        name="Not Updated"
        if request.user.first_name!='' or request.user.last_name!='':
            name=request.user.first_name+request.user.last_name

        Session=Session_Details(date=datetime.datetime.now(),
                                Session_Name=Session_Name,
                                Branch=b[:-1],
                                year=y[:-1],
                                role=r,
                                NameOfTest=NameOfTest,
                                QuizCreator=request.user.username,
                                QuizCreatorName=name)
        

        Session.save()
        session=Session_Details.objects.latest("date")
        context={'session':session,'QuizName':NameOfTest}

        return redirect('/CreateQuiz/'+session.slug)
    if request.method == 'POST':
        print(request.POST.get("start"))
        if request.POST.get("start"):
            quiz=get_object_or_404(QuizList,NameOfTest=request.POST.get("start"))
            quiz.position=1
            quiz.save()

        elif request.POST.get("stop"):
            quiz=get_object_or_404(QuizList,NameOfTest=request.POST.get("stop"))
            quiz.position=0
            quiz.save()
        return redirect('/')
    return render(request,'index.html',context)

    
@login_required
def Profile(request):
    if request.method == 'POST':
        u_form = CustomUserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
    else:
        u_form = CustomUserUpdateForm(instance=request.user)

    context = {'u_form': u_form}
    return render(request, 'profile.html', context)

def ProfileView(request,slug):
    # print("yes")
    label=[]
    data=[]
    data1=[]
    students=get_object_or_404(get_user_model(),username=slug)
    print(students)
    leaderboard=LeaderBoard.objects.filter(rollno=slug)
    queryset=leaderboard
    for i in queryset:
        label.append(i.test)
        data.append(i.securedscore)
        data1.append(i.wrong_answer)
    Correct={
        'name':'correct',
        'data':data,
        'color':'green',
    }
    Wrong={
        'name': 'wrong/unattmpeted',
        'data':data1,
        'color':'red',
    }
    chart = {
        'chart': {'type': 'line'},
        'title': {'text': "Student's statistics"},
        'yAxis': {'title': {'text': "Score's" }},
        'xAxis': {'categories': label},
        'legend': {'layout': 'vertical','align': 'right',
        'verticalAlign': 'middle'},
        'series': [Correct,Wrong],
        'plotOptions': {
        'line': {
            'dataLabels': {
                'enabled': 'true'
            },
            'enableMouseTracking': 'false'
        }
    },
        'responsive': {'rules': [{
            'condition': {
                'maxWidth': '100'
            },
            'chartOptions': {
                'legend': {
                    'layout': 'horizontal',
                    'align': 'center',
                    'verticalAlign': 'bottom'
                }
            }
        }]
    }
    }


    dump = json.dumps(chart)
    context={'leaderboard':leaderboard,'students':students,'labels': label,
        'data': data,'chart':chart}


    return render(request,'profileView.html',context)
    
def Testing(request):
    return render(request,'login.html')

@login_required
def Table(request):
    students=get_user_model().objects.all()
    dic={}
    for i in students:
        x=list(LeaderBoard.objects.filter(rollno=i.username))
        for i in x:
            if i.rollno not in dic:
                dic[i.rollno]=i.totalscore,i.securedscore
            else:
                x,y=dic[i.rollno][0],dic[i.rollno][0]

                dic[i.rollno]=(x+i.totalscore,y+i.securedscore)
    dic = sorted(dic.items(), key=lambda x: x[1][1], reverse=True)
    print(dic)
    context={'dic':dic,'students':students}
    return render(request,'table.html',context)

def DailyScoreBoard(request,slug):
    leaderboard=LeaderBoard.objects.all().order_by('-securedscore')
    users = User.objects.all()
    label=get_object_or_404(Label,slug=slug)
    
    context={'leaderboard':leaderboard,'label':label,'students':students}
    return render(request,'scores.html',context)

def RedirectLabOrQuiz(request,slug):
    session=get_object_or_404(Session_Details,slug=slug)
    if session.TypeOfExam=="Q":
        PreviewQuizCreating(request,slug)
        return
    else:
        pass
        

def statofstudent(request,slug):
    label=[]
    data=[]
    data1=[]
    students=get_object_or_404(Student_Details,slug=slug)
    print(students)
    leaderboard=LeaderBoard.objects.filter(rollno=students.Rollno)
    queryset=leaderboard

    for i in queryset:
        label.append(i.test)
        data.append(i.securedscore)
        data1.append(i.wrong_answer)
    Correct={
        'name':'correct',
        'data':data,
        'color':'green',
    }
    Wrong={
        'name': 'wrong/unattmpeted',
        'data':data1,
        'color':'red',
    }
    chart = {
        'chart': {'type': 'line'},
        'title': {'text': "Student's statistics"},
        'yAxis': {'title': {'text': "Score's" }},
        'xAxis': {'categories': label},
        'legend': {'layout': 'vertical','align': 'right',
        'verticalAlign': 'middle'},
        'series': [Correct,Wrong],
        'plotOptions': {
        'line': {
            'dataLabels': {
                'enabled': 'true'
            },
            'enableMouseTracking': 'false'
        }
    },
        'responsive': {'rules': [{
            'condition': {
                'maxWidth': '100'
            },
            'chartOptions': {
                'legend': {
                    'layout': 'horizontal',
                    'align': 'center',
                    'verticalAlign': 'bottom'
                }
            }
        }]
    }
    }


    dump = json.dumps(chart)
    context={'leaderboard':leaderboard,'students':students,'labels': label,
        'data': data,'chart':chart}


    return render(request,'stats.html',context)

