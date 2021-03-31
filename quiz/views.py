from django.shortcuts import render,get_object_or_404,redirect
from students.models import *
from .models import *
from django.views.decorators.csrf import csrf_exempt
import json,csv,os
from django.core import serializers
from django.contrib import messages
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.conf import settings
from csv import writer
@csrf_exempt
def PreviewQuizCreating(request,slug):
    session=get_object_or_404(Session_Details,slug=slug)
    context={'session':session}
    if request.method == 'POST':
        
        json_data = json.loads(request.body.decode())
        cnt=0
        print(json_data)
        if Quiz.objects.filter(NameOfTest=session.NameOfTest):
            Quiz.objects.all().filter(NameOfTest=session.NameOfTest).delete()
            QuizList.objects.filter(NameOfTest= session.NameOfTest).delete()
        for i in range(2,len(json_data)):
            cnt+=1
            lst=['a','b','c','d']
            if json_data[i]["correctAnswer"] in lst:
                  json_data[i]["correctAnswer"]=chr(ord(json_data[i]["correctAnswer"])-32)
            name="Not Updated"
            if request.user.first_name!='' or request.user.last_name!='':
                name=request.user.first_name+request.user.last_name
            quizcheck=Quiz.objects.all()
            tim=request.POST.getlist('option')
            tie=request.POST.get('Quiz_name')
            time=request.POST.get('quizduration')
            print(tim,tie,time)
            Quiz_Save=Quiz(QuizCreator=request.user.username,
                        QuizCreatorName=name,
                        Session_Name=session.Session_Name,
                        NameOfTest=session.NameOfTest,
                        Question=json_data[i]["question"],
                        option1=json_data[i]["answers"]['a'],
                        option2=json_data[i]["answers"]['b'],
                        option3=json_data[i]["answers"]['c'],
                        option4=json_data[i]["answers"]['d'],
                        option5=json_data[i]["answers"]['e'],
                        Answer=json_data[i]["correctAnswer"]
                        )

            Quiz_Save.save()

            
        if json_data[1]["quizduration"]["type"] == "Minutes":
            ModeOfTime="Minutes"
            time=int(json_data[1]["quizduration"]["time"])*60
        elif json_data[1]["quizduration"]["type"] == "Hours":
            ModeOfTime="Hours"
            time=int(json_data[1]["quizduration"]["time"])*60*60
        else:
            ModeOfTime="Seconds"
            time=int(json_data[1]["quizduration"]["time"])
            
        QuizList_save=QuizList(Session_Name=session.Session_Name,
                        NameOfTest=session.NameOfTest,
                        NumberOfQuestions=cnt,
                        Time=time,
                        ModeOfTime=ModeOfTime
                        )   
        QuizList_save.save()
    QuizName=session.NameOfTest
    context={'session':session,'QuizName':QuizName}
    return render(request,'CQ.html',context)
@csrf_exempt
def PreviewQuizWriting(request,slug):
    lst=slug.split("23we",3)
    session=Session_Details.objects.filter(slug=slug[:-1])
    quizlist=QuizList.objects.filter(slug=slug)
    quizlist=get_object_or_404(QuizList,slug=slug)
    time=quizlist.Time
    Quiz_Save=Quiz.objects.all().filter(NameOfTest=lst[1]).values('Question','option1','option2','option3','option4','option5',).all();
    result=list(Quiz_Save)
    mydata=json.dumps(result)
    print(mydata)
    print("ho",quizlist.position)
    context={'quizlist':quizlist,'Quiz':Quiz_Save,'session':session,
    'Questions':mydata,'head':lst[1],'time':time}

    if quizlist.position==1:
        print("hop",request.method)
        if request.method== "POST":
            print("hop")
            data=request.body.decode()
            print(data)
            cnt=0
            Quiz_Answers=list(Quiz.objects.all().filter(NameOfTest=lst[1]).values('Answer').all())
            lst_ans=[]
            d=['RollNo',"data"]
            for j,i in enumerate(Quiz_Answers):
                d.insert(-1,str(j+1)+"-Answer")
                lst_ans.append(i["Answer"])
            data=eval(data)
            totalscore,securedscore,correct_answer,wrong_answer=0,0,0,0
            for i in range(1,len(lst_ans)+1):
                totalscore+=1

                if lst_ans[i-1]==chr(ord(data[str(i)])-32):

                    correct_answer+=1
                else:
                    wrong_answer+=1
            securedscore=correct_answer
            dic={str(request.user):{"data":data,"correct_answer":correct_answer,"wrong_answer":wrong_answer,"securedscore":securedscore}}

            LeaderBoard_save=LeaderBoard(
                rollno_test=request.user.username+lst[1],
                rollno=request.user.username,
                test=lst[1],
                totalscore=totalscore,
                securedscore=securedscore,
                correct_answer=correct_answer,
                wrong_answer=wrong_answer,

            )
            lead=[request.user.username,totalscore,correct_answer,wrong_answer,data]
            LeaderBoard_save.save()
            g=0
            try:
                with open('CSV/'+str(lst[1])+'.csv', 'r+') as f:
                    reader = csv.reader(f)
                    if list(reader)[0]==d:
                        g=1
                    else:
                        g=0
            except:
                with open('CSV/'+str(lst[1])+'.csv', 'a') as f:
                    write=writer(f)
                    if g==0:
                        write.writerow(d)
                    write.writerow(lead)
                


        return render(request,'OrginalQuiz.html',context)
    else:
        messages.warning(request, 'Test is not activated wait till it is actived')
        return redirect('/')

def EditQuiz(request,slug):
    lst=slug.split("23we",3)
    print(lst,"ho")
    if get_object_or_404(QuizList,NameOfTest=lst[1]) :
        print("no")
        Quiz_Save=get_object_or_404(QuizList,NameOfTest=lst[1])
        return redirect('/EditQuizRedirect/'+Quiz_Save.slug)
    else :

        print("hno")
        return redirect('/CreateQuiz/'+slug)
        
@csrf_exempt
def EditQuiz1(request,slug):
    lst=slug.split("23we",3)
    session=get_object_or_404(Session_Details,slug=slug[:-1])
    Quiz_Save=Quiz.objects.all().filter(NameOfTest=lst[1]).values('Question','option1','option2','option3','option4','option5','Answer').all();
    mydata=json.dumps(list(Quiz_Save))
    quizlist=get_object_or_404(QuizList,slug=slug)
    time=quizlist.Time
    mode=quizlist.ModeOfTime
    print(time,mode,mydata)
    context={'mydata':mydata,'quizlist':quizlist,'time':time
    ,'session':session,'mode':mode}
    if request.method == 'POST':
        
        json_data = json.loads(request.body.decode())
        cnt=0
        print(json_data)
        if Quiz.objects.filter(NameOfTest=session.NameOfTest):
            Quiz.objects.all().filter(NameOfTest=session.NameOfTest).delete()
            QuizList.objects.filter(NameOfTest= session.NameOfTest).delete()
        for i in range(2,len(json_data)):
            cnt+=1
            lst=['a','b','c','d']
            if json_data[i]["correctAnswer"] in lst:
                  json_data[i]["correctAnswer"]=chr(ord(json_data[i]["correctAnswer"])-32)
            name="Not Updated"
            if request.user.first_name!='' or request.user.last_name!='':
                name=request.user.first_name+request.user.last_name
            quizcheck=Quiz.objects.all()
            tim=request.POST.getlist('option')
            tie=request.POST.get('Quiz_name')
            time=request.POST.get('quizduration')
            print(tim,tie,time)
            Quiz_Save=Quiz(QuizCreator=request.user.username,
                        QuizCreatorName=name,
                        Session_Name=session.Session_Name,
                        NameOfTest=session.NameOfTest,
                        Question=json_data[i]["question"],
                        option1=json_data[i]["answers"]['a'],
                        option2=json_data[i]["answers"]['b'],
                        option3=json_data[i]["answers"]['c'],
                        option4=json_data[i]["answers"]['d'],
                        option5=json_data[i]["answers"]['e'],
                        Answer=json_data[i]["correctAnswer"]
                        )

            Quiz_Save.save()

            
        if json_data[1]["quizduration"]["type"] == "Minutes":
            time=int(json_data[1]["quizduration"]["time"])*60
        elif json_data[1]["quizduration"]["type"] == "Hours":
            time=int(json_data[1]["quizduration"]["time"])*60*60
        else:
            time=int(json_data[1]["quizduration"]["time"])
        QuizList_save=QuizList(Session_Name=session.Session_Name,
                        NameOfTest=session.NameOfTest,
                        NumberOfQuestions=cnt,
                        Time=time
                        )   
        QuizList_save.save()
    QuizName=session.NameOfTest
    context={'mydata':mydata,'quizlist':quizlist,'time':time
    ,'session':session,'mode':mode,'QuizName':QuizName}
    return render(request,'CQEdit.html',context)

def EndQuiz(request):

    return render(request,'EndQuiz.html')


