from django.contrib import admin
from django.conf.urls import url,include
from meeting_app import views
from django.conf import settings






urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    url(r'^sendmail/',views.sendmail,name='sendmail'),
    url(r'^meeting_app/',include('meeting_app.urls', namespace='meeting_app')),
    url(r'^logout/$',views.user_logout,name='logout'),
    url(r'special/',views.special,name='special'),


]
