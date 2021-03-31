from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Student, Lecturer, CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', ]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Student)
admin.site.register(Lecturer)
