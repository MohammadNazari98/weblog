from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^posts/$', views.posts),
    url(r'^login/$', views.LoginView.as_view()),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<title>[a-zA-Z ]*)/$', views.post),
]
