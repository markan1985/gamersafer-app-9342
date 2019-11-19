from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.db.models import CharField
from django.db import models

from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    country = CharField(_("Country"), blank=True, null=True, max_length=255)
    # state = CharField(_("State"), blank=True, null=True, max_length=255)
    # dob = CharField(_("dob of User"), blank=True, null=True, max_length=255)
    # face_data = CharField(_("face data of User"), blank=True, null=True, max_length=255)
    name = CharField(_("name of User"), blank=True, null=True, max_length=255)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

class Preferences(models.Model):
    interaction = CharField( blank=True, null=True, max_length=255)
    streaming = CharField(blank=True, null=True, max_length=255)
    playstyle = CharField( blank=True, null=True, max_length=255)
    usagepattern = CharField(  blank=True, null=True, max_length=255)
    user_id = CharField(  blank=True, null=True, max_length=255)
    
