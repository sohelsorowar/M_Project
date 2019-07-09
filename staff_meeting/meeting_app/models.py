from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User,on_delete=models.PROTECT)


    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

def __str__(self):
    return self.user.username



class Create_Meeting(models.Model):
    meeting_id = models.IntegerField()
    meeting_name= models.CharField(max_length=256)
    meeting_sub= models.CharField(max_length=256)
    meeting_text= models.TextField(max_length=1024)

    def __str__(self):
        return self.meeting_name

    def get_absolute_url(self):
        return reverse("meeting_app:meeting_detail", kwargs={'pk': self.pk})

        #return reverse("meeting_app:meeting_detail")


# Create your models here.
