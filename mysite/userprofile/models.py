from django.db import models
from django.db.models.signals import post_save
from Accounts.models import NewUsers
# Create your models here.
class UserProfile(models.Model):
    fname = models.CharField(max_length=12, default='First Name')
    lname = models.CharField(max_length=12, default='Last Name')
    user = models.OneToOneField(NewUsers, on_delete=models.CASCADE)
    profile_image = models.ImageField(default='avatar.png', upload_to='profile')
    cover = models.ImageField(default='cover.png', upload_to='cover')
    bio = models.TextField(default='Your Bio')
    joined = models.DateTimeField(auto_now_add=True)
    dob = models.CharField(max_length=12,default='DD-MM-YYYY')

    profile_status = models.CharField(max_length=20, verbose_name='Activate')



    def __str__(self):
        return self.user.username + " - " + self.joined.strftime('%d-%m-%y')


def create_user_profile(sender, instance, created, **kwargs):
    print("Sender:", sender)
    print("Instance:", instance, type(instance))
    print("Crearted:", created)
    print("kwargs:", kwargs)
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=NewUsers)