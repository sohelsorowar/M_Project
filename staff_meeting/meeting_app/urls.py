from django.conf.urls import url
from meeting_app import views

app_name ='meeting_app'
urlpatterns=[
       url(r'^$',views.Create_MeetingListView.as_view(),name='list'),
       url(r'^register/$',views.register,name='register'),
       url(r'^user_login/$',views.user_login,name='user_login'),
       url(r'^create_meeting/$',views.Create_MeetingCreateView.as_view(),name='create_meeting'),
       url(r'^update/(?P<pk>\d+)/$',views.Create_MeetingUpdateView.as_view(),name='update'),
        url(r'^delete/(?P<pk>\d+)/$',views.Create_MeetingDetailView.as_view(),name='delete'),
       url(r'^(?P<pk>\d+)/$',views.Create_MeetingDetailView.as_view(),name='meeting_detail'),
       url(r'^meeting_detail/$',views.meeting_detail,name='meeting_detail'),

      # url(r'^$',views.Create_MeetingListView.as_view,name='list')
 ]
