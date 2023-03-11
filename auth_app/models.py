from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfileInfo(models.Model):

    # Creating relationship
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    # Adding any additional attributes you would like
    portfolio_site = models.URLField(blank=True)
    
    profile_picture = models.ImageField(upload_to='profile_picture',blank=True)

    def __str__(self):
        return self.user.username