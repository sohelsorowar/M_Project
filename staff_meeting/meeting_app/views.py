from django.shortcuts import render
from meeting_app.forms import UserForm,UserProfileInfoForm
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from . import models
from django.core.mail import send_mail
from django.conf import settings
from .forms import Create_MeetingForm







# Create your views here.
def index(request):
    return render(request,'meeting_app/index.html')

def sendmail(request):

    if request.method=='POST':
        message = request.POST['message']
        subject = request.POST['subject']
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['sohelsorowar@gmail.com','sohelsorowar@ru.ac.bd',13055417]
        #print('request', request.POST)
        #members = models.Committee_Member.objects.get(type=Committee_Member.email)
        #recipient_list = ['members',]
        #for member in members:
        #    recipient_list.append(member.email)


        send_mail( subject, message, email_from, recipient_list,fail_silently=False)
        return HttpResponse("Mail send successfully")








def create_meeting(request):
    return render(request,'meeting_app/create_meeting.html')

def meeting_detail(request):
    return render(request,'meeting_app/meeting_detail.html')



@login_required
def special(request):
    return HttpResponse("you are logged in !!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False

    if request.method =="POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)


        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']


            profile.save()

            registered = True
        else:
                print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'meeting_app/registration.html',
                               {'user_form':user_form,
                                'profile_form':profile_form,
                                 'registered':registered})






def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
                #return render(request,'meeting_app/create_meeting.html')
            else:
                return HttpResponse("Account not Active!!!")
        else:
            print("Someone tried to login and failed")
            print("Username: {} and password: {}".format(username,password))
            return HttpResponse("Invalied login!!")
    else:
        return render(request,'meeting_app/login.html',{})


class Create_MeetingListView(ListView):
    context_object_name = 'create_meetings'
    model = models.Create_Meeting

class Create_MeetingDetailView(DetailView):
    context_object_name = 'meeting_detail'
    model = models.Create_Meeting
    template_name = 'meeting_app/meeting_detail.html'

class Create_MeetingCreateView(CreateView):
    fields=('meeting_name','meeting_sub','meeting_text','date')
    model = models.Create_Meeting

class Create_MeetingUpdateView(UpdateView):
    fields=('meeting_name','meeting_sub','meeting_text','date')
    model = models.Create_Meeting


class Create_MeatingDeleteView(DeleteView):

    model = models.Create_Meeting
    success_url = reverse_lazy("meeting_app:list")


class Committee_MemberListView(ListView):
    context_object_name = 'committee_members'
    model = models.Committee_Member

# resulations

class ResulationListView(ListView):
        context_object_name = 'resulations'
        model = models.Resulation

#lass Create_MeetingListView(DetailView):
#    context_object_name='meeting_detail'
#    model = models.Create_Meeting
#    template_name = 'meeting_app/meeting_detail.html'
