from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import datetime

# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User,on_delete=models.PROTECT)


    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

def __str__(self):
    return self.user.username

CHOICES = (
    ('Planning Meeting','Planning Meeting',),
    ('Exam Committee Meeting', 'Exam Committee Meeting'),
    ('Event Meeting','Event Meeting'),
    ('AC Meeting','AC Meeting'),
    ('General Meeting','General Meeting'),
    ('Other','Other')
)

class Create_Meeting(models.Model):
    #meeting_id = models.IntegerField()
    meeting_id = models.AutoField(primary_key=True)
    meeting_name= models.CharField(max_length=256, choices=CHOICES, default='General Meeting')
    meeting_sub= models.CharField(max_length=256)
    meeting_text= models.TextField(max_length=500)
    date = models.DateField(default=datetime.now)

    def __str__(self):
        return self.meeting_name

    def get_absolute_url(self):
        return reverse("meeting_app:meeting_detail", kwargs={'pk': self.pk})

        #return reverse("meeting_app:meeting_detail")


class Committee_Member(models.Model):
    first_name = models.CharField(max_length=50,blank=False)
    last_name = models.CharField(max_length=50,blank=False)
    designation = models.CharField(max_length=50,blank=False)
    member_type = models.ForeignKey(Create_Meeting,related_name='committee_members')
    email = models.EmailField(max_length=70,blank=False)

    def __str__(self):
        return self.first_name



# Create your models here.
