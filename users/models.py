from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group

class CustomUser(AbstractUser):
    pass

    @property
    def is_student(self):
        try:
            return bool(self.student)
        except ObjectDoesNotExist:
            return False

    @property
    def is_lecturer(self):
        try:
            return bool(self.lecturer)
        except ObjectDoesNotExist:
            return False


class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,
                                related_name='student')
    slug = models.SlugField(unique=True,null=False)


    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('ProfileView', kwargs={'slug': self.slug})
    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.user)
        super(Student,self).save()



    class Meta:
        verbose_name = _('Student')
        verbose_name_plural = _('Students')


class Lecturer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,
                                related_name='lecturer')
    subject = models.CharField(max_length=256, blank=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _('Lecturer')
        verbose_name_plural = _('Lecturers')
