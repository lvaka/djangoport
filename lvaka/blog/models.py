# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

"""class Project(models.Model):
	author = models.ForeignKey('auth.User')
	site_name = models.CharField(max_length=140)
	site_url = models.CharField(max_length=400)
	img_url = models.CharField(max_length=400)
	languages = models.TextField()

	def publish(self):
		self.save()

	def __str__(self):
		return self.site_name"""