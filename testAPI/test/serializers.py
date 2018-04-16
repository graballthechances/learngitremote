# -*- coding: utf-8 -*-
'''
'''

from django.contrib.auth.models import User,Group
from rest_framework import serializers
from models import firstMysqlModel

class firstSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=firstMysqlModel
		fields=('url','username','hobby')
#
# class GroupSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model=Group
# 		fields=('url','name')