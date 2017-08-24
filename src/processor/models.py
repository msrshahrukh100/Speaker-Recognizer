# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.dispatch import receiver
import os
from django.db import models

# Create your models here.
def upload_location(instance, filename):
    return "%s/%s/%s" %("data",instance.name, filename)


class UserInfo(models.Model) :
	name = models.CharField(max_length=100,null=False, blank=False, unique=True)
	voice = models.FileField(upload_to=upload_location, null=False, blank=False)

	def __unicode__(self) :
		return str(self.id)

def temp_location(instance, filename) :
	return "%s/%s" %("temp", filename)

class Temp(models.Model) :
	name = models.CharField(max_length=100,null=False, blank=False)
	voice = models.FileField(upload_to=temp_location, null=False, blank=False)

	def __unicode__(self) :
		return str(self.id)


@receiver(models.signals.post_delete, sender=Temp)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.voice:
        if os.path.isfile(instance.voice.path):
            os.remove(instance.voice.path)

