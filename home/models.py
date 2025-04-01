# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Clienti(models.Model):

    #__Clienti_FIELDS__
    nume = models.TextField(max_length=255, null=True, blank=True)
    telefon = models.TextField(max_length=255, null=True, blank=True)
    adresa = models.TextField(max_length=255, null=True, blank=True)

    #__Clienti_FIELDS__END

    class Meta:
        verbose_name        = _("Clienti")
        verbose_name_plural = _("Clienti")


class Aviz(models.Model):

    #__Aviz_FIELDS__
    nrcrt = models.IntegerField(null=True, blank=True)
    muncii = models.CharField(max_length=255, null=True, blank=True)
    transporturi = models.CharField(max_length=255, null=True, blank=True)
    securitatii = models.CharField(max_length=255, null=True, blank=True)

    #__Aviz_FIELDS__END

    class Meta:
        verbose_name        = _("Aviz")
        verbose_name_plural = _("Aviz")



#__MODELS__END
