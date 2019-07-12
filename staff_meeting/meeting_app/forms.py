from django import forms
from django.contrib.auth.models import User
from meeting_app.models import UserProfileInfo,Create_Meeting

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())


    class Meta():
        model = User
        fields = ('username','first_name','last_name','email','password')

class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')


class Create_MeetingForm(forms.ModelForm):
    class Meta():
        model = Create_Meeting
        fields =('meeting_name','meeting_sub','meeting_text','date')
