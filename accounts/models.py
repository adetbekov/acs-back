from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def upload_location(instance,filename):
    return "%s/%s" %(instance.id,filename)

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    birth = models.DateField(null=True)
    phone = models.CharField(max_length=12, null=True)
    image = models.ImageField(null=True, blank=True, upload_to=upload_location)



User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])

# class Activate(models.Model):
#     user=models.OneToOneField(User)
#     hash=models.CharField(max_length=255)
#     assigned_date=models.DateField(auto_now=False,auto_now_add=True)

#     class Meta:
#         verbose_name = 'Активация'
#         verbose_name_plural = 'Активации'
    
# class Reset(models.Model):
#     user=models.OneToOneField(User)
#     hash=models.CharField(max_length=255)
#     assigned_date=models.DateField(auto_now=False,auto_now_add=True)

#     class Meta:
#         verbose_name = 'Восстановление пароля'
#         verbose_name_plural = 'Восстановления паролей'
