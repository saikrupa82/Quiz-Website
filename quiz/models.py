from django.db import models
from users.models import *
from students.models import *
import time
class Quiz(models.Model):
    QuizCreator=models.CharField(max_length=200)
    QuizCreatorName=models.CharField(max_length=200,blank=True)
    Session_Name=models.CharField(max_length=200)
    NameOfTest = models.CharField(max_length=200)
    Question=models.CharField(max_length=20000,blank=False)
    option1=models.CharField(max_length=2000,blank=True)
    option2=models.CharField(max_length=2000,blank=True)
    option3=models.CharField(max_length=2000,blank=True)
    option4=models.CharField(max_length=2000,blank=True)
    option5=models.CharField(max_length=2000,blank=True)
    Answer=models.CharField(max_length=1,blank=False)

    class Meta:
        unique_together = (('Session_Name','NameOfTest','Question'))

class QuizList(models.Model):
    Session_Name=models.CharField(max_length=200)
    NameOfTest = models.CharField(max_length=200)
    NumberOfQuestions = models.IntegerField(default=0)
    Time = models.CharField(max_length=100,blank=True,default=0)
    position=models.BooleanField(default=0,blank=False)
    slug = models.SlugField(unique=True,null=False)
    ModeOfTime = models.CharField(max_length=200,null=True)

    def save(self, *args, **kwargs):
        test=''
        if not self.slug:
            for i in self.Session_Name:
                if i==' ':
                    test+='-'
                else:
                    test+=i
            test+='23we'

            for i in self.NameOfTest:
                if i==' ':
                    test+='-'
                else:
                    test+=i
            test+='23we'

            test+=str(self.NumberOfQuestions)
            self.slug = slugify(test)
        super(QuizList,self).save()


    def get_absolute_url(self):
        return reverse('PreviewQuizWriting', kwargs={'slug': self.slug})

    class Meta:
        unique_together = (('Session_Name','NameOfTest','NumberOfQuestions'))