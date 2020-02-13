from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    name = models.CharField(null=True, blank=True, max_length=255,)
    test = models.BigIntegerField(null=True, blank=True,)
    ghhg = models.CharField(max_length=256, null=True, blank=True,)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class Test(models.Model):
    "Generated Model"
    test = models.BigIntegerField()
    testtt = models.BigIntegerField(null=True, blank=True,)
    gfg = models.BigIntegerField(null=True, blank=True,)
