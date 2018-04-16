 # -*- coding: utf-8 -*
from django.db import models
# from django.core.urlsolvers import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# from django.conf import settings


# Create your models here.
class up(models.Model):#查询中的余额
	user=models.OneToOneField(User,related_name='up')
	yuan_balance=models.IntegerField(default=0)
	dollar_balance=models.IntegerField(default=0)
	hk_balance=models.IntegerField(default=0)
	annuity=models.IntegerField(default=0)

	def change_yuan(self,yuan):
		self.yuan_balance=yuan
		self.save()
	
	def change_dollar(self,dollar):
		self.dollar_balance=dollar
		self.save()

	def change_hk(self,hk):
		self.hk_balance=hk
		self.save()


class ecash(models.Model):#电子现金
	user=models.OneToOneField(User)
	e_balance=models.IntegerField(default=0)

	def change_ecash(self,ecash):
		self.e_balance=ecash
		self.save()

# class fund(models.Model):#公积金
# 	user=models.OneToOneField(User)
# 	balance_all=models.CharField(max_length=200)
# 	last_year_balance=models.CharField(max_length=200)


