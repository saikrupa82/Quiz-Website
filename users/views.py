from django.shortcuts import render, redirect
from .forms import studentForm, studentAddForm, teacherForm, teacherAddForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .models import Student, Lecturer
from django.contrib.auth.models import User
from .decorators import login_student_required, login_lecturer_required


def index(request):
    return render(request, 'users/index.html')


@login_required
def userLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def userLogin(request):
    invalidlogin = False
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/users/index')
            else:
                return HttpResponse('Account not active')
        else:
            invalidlogin = True
            return redirect('/users/login/')
    else:
        return render(request, 'users/login.html', {'invalidlogin': invalidlogin})


@login_student_required
def student_index(request):
    return render(request, 'users/studentDash.html', context={'student': request.user})


@login_lecturer_required
def lecturer_index(request):
    return render(request, 'users/teacherDash.html', context={'lecturer': request.user})
