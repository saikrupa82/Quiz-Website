
from django import forms
from .models import LeaderBoard
from users.models import CustomUser

class LeaderBoardData(forms.Form):
	class meta:
		model = LeaderBoard
		exclude = ['id']
class CustomUserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name']
