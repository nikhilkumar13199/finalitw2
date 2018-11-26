# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class Entries(models.Model):
    @property
    def user(self):
        return User.objects.get(pk=self.user_id)

class top5users(models.Model):
	username=models.CharField(max_length=30)
	totalup=models.IntegerField()
	totaldo=models.IntegerField()
	totalpo=models.IntegerField()

class latest_posts(models.Model):
	pid=models.IntegerField()
	uid=models.IntegerField()
	upvotes=models.IntegerField()
	downvotes=models.IntegerField()
	content=models.CharField(max_length=2451)
	


	# def get_absolute_url(self):
	# 	return "/rssfeed/%i/" % self.id
		# from django.urls import reverse
		# return reverse('museo:feed',kwargs={'content':self.content,'post_id':self.id})
	# def get_absolute_url(self):
 #    	return reverse('museo:feed', kwargs={'section': self.content.section_url,'post_id': self.id})

	# @permalink
 #    def get_absolute_url(self):
 #        if not self.passthrough_page:
 #            return 'view_page', None, {'slug': self.slug}
 #        else:
 #            return self.passthrough_link
