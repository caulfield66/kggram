from django.db import models
from django.contrib.auth.models import User

from post.models import Post
from django.db.models.signals import post_save

from PIL import Image
from django.conf import settings
import os


def user_directory_path(instance, filename):
    profile_pic_name = 'user_{0}/profile.jpg'.format(instance.user.id)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_pic_name)

    if os.path.exists(full_path):
        os.remove(full_path)

    return profile_pic_name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    url = models.CharField(max_length=80, null=True, blank=True)
    profile_info = models.TextField(max_length=150, null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    favorites = models.ManyToManyField(Post)
    picture = models.ImageField(upload_to='user_directory_path', blank=True, null=True, verbose_name='Picture')
    # is_staff = models.BooleanField(default=False)
    # is_superuser = models.BooleanField(default=False)

    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def has_module_perms(self, app_label):
        return self.is_staff or self.is_superuser


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
