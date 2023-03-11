from basicform_app import views
from django.urls import re_path


urlpatterns = [
    re_path(r'^$', views.form_user_view, name='form_users'),
]