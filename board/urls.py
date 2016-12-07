from django.conf.urls import url
from board import views

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^events/$', views.EventList.as_view()),
    url(r'^events/(?P<pk>[0-9]+)/vote/$', views.VoteViewSet.as_view()),
    url(r'^events/(?P<pk>[0-9]+)/$', views.EventDetail.as_view()),
]
