from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


def upload_location(instance, filename):
	filebase, extension = filename.split(".")
	return "%s/%s.%s" %(instance.id, instance.id, extension)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar= models.ImageField(upload_to="avatar", null=True, blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    phone = models.IntegerField(blank=True, null=True)
    adress = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    objects = models.Manager()


    def  __str__(self):
        return str(self.user)

def post_save_user_receiver(sender, instance, created, *args, **kwargs):
    if created:
        new_profile = UserProfile.objects.get_or_create(user=instance)


post_save.connect(post_save_user_receiver, sender =User)