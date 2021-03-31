from django.db import models
import datetime
from django.urls import reverse
from django.template.defaultfilters import slugify # new
class Session_Details(models.Model):
    role=(
        ('Q','Quiz'),
        ('L','Lab')
    )
    date=models.DateTimeField(default=datetime.datetime.now())
    Session_Name=models.CharField(max_length=200,primary_key=True)
    Branch=models.CharField(max_length=200)
    year=models.CharField(max_length=200)
    slug = models.SlugField(unique=True,null=False)
    role = models.CharField(blank=True,max_length=1,choices=role)
    NameOfTest = models.CharField(max_length=200)
    QuizCreator=models.CharField(max_length=200)
    QuizCreatorName=models.CharField(max_length=200,blank=True)
    
    def save(self, *args, **kwargs):
        test=''
        if not self.slug:
            for i in self.Session_Name:
                if i==' ':
                    test+='-'
                else:
                    test+=i
            test+='23@we'
            for i in self.NameOfTest:
                if i==' ':
                    test+='-'
                else:
                    test+=i
            test+='23@we'
            self.slug = slugify(test)
        super(Session_Details,self).save()

    def get_absolute_url(self):
        return reverse('SesssionOnView', kwargs={'slug': self.slug})

    class Meta:
        unique_together = (('Session_Name','NameOfTest'))

class Student_Details(models.Model):
    role=(
        ('F','Faculty'),
        ('S','Student')
    )
    Rollno=models.CharField(max_length=10,primary_key=True)
    Name=models.CharField(max_length=200)
    slug = models.SlugField(unique=True,null=False)
    role = models.CharField(blank=True,max_length=1,choices=role)

    def get_absolute_url(self):
        return reverse('stats', kwargs={'slug': self.slug})
    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.TestName)
        super(Student_Details,self).save()

    def __str__(self):
        return f'{self.Name} {self.Rollno}'


class Label(models.Model):
    TestName=models.CharField(primary_key=True, editable=False,max_length=200)
    date=models.DateField(default=datetime.date.today)
    Students=models.IntegerField()
    slug = models.SlugField(unique=True,null=False)

    def get_absolute_url(self):
        return reverse('score', kwargs={'slug': self.slug})
    def save(self, *args, **kwargs):
        test=''
        if not self.slug:
            for i in self.TestName:
                if i==' ':
                    test+='-'
                else:
                    test+=i
            self.slug = slugify(test)
        super(Label,self).save()

    
class LeaderBoard(models.Model):
    rollno_test=models.CharField(max_length=210,primary_key=True)
    rollno=models.CharField(editable=False,max_length=10)
    test=models.CharField(max_length=200)
    totalscore=models.FloatField()
    securedscore=models.FloatField()
    correct_answer=models.IntegerField()
    wrong_answer=models.IntegerField()
    date=models.DateField(default=datetime.date.today)
    
    def __str__(self):
        return self.rollno
    class Meta:
        unique_together = (('rollno','test'))
