from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField as PuIf


# Create your models here.

class BaseModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Person(BaseModel):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    profile_picture = PuIf(blank=True, null=True, manual_crop='')
    due_amount = models.IntegerField(default=0)
    card_number = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=200, null=True, blank=True)
    about = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username
