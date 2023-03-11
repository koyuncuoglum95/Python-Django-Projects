from urlapp import views
from django.urls import re_path


app_name = 'url_app'

urlpatterns = [
    re_path(r'^relative/$', views.relative,name='relative'),
    re_path(r'^other/$',views.other,name='other'),
]