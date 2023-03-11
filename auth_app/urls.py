from django.urls import re_path
from auth_app import views


app_name = 'auth_app'

urlpatterns = [
    re_path(r'^register/$', views.register,name='register'),
    re_path(r'^user_login/$', views.user_login,name='user_login'),
    re_path(r'^user_logout/$', views.user_logout,name='user_logout'),
]
