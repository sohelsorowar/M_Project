from django.contrib import admin
from django.conf.urls import url,include
from meeting_app import views


urlpatterns = [
    url(r'^$',views.index,name='index'),
    url('admin/', admin.site.urls),
    url(r'^meeting_app/',include('meeting_app.urls', namespace='meeting_app')),
    url(r'^logout/$',views.user_logout,name='logout'),
    url(r'special/',views.special,name='special')
]
