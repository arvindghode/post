# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	title = models.CharField(max_length=250)
	body = models.TextField()
	added_by = models.ForeignKey(User, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['created']
		verbose_name = "Post"
		verbose_name_plural = "Posts"

	def __unicode__(self):
		return self.title

class Comment(models.Model):
	post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
	added_by = models.ForeignKey(User, on_delete=models.CASCADE)
	comment = models.TextField()
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['created']
		verbose_name = "Comment"
		verbose_name_plural = "Comments"



