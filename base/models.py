from django.db import models
from django.utils import timezone
from multiselectfield import MultiSelectField
now = timezone.now()

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.urls import reverse


class User(models.Model):
    user =models.TextField(default=None)
    def __str__(self):
        return self.user

class LatestPost(models.Model):
    MY_CHOICES = ((1, 'Programming'),
              (2, 'Technology'),
              (3, 'International'),
              (5, 'IT')
              )
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_pic = models.ImageField(default='welcome.gif',null=True,blank=True)
    category = MultiSelectField(choices=MY_CHOICES,
                         max_choices=4,
                         max_length=30,null=True,blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    header = models.BooleanField(blank=True,null=True,default=True)
    published = models.DateTimeField(default=timezone.now, verbose_name="published date",)



    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('latestpost',
                       args=[self.id])    








