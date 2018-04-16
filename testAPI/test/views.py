# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from rest_framework.response import Response
from django.shortcuts import render
# from django.contrib.auth.models import User,Group
from rest_framework import viewsets,permissions,authentication
# from models import firstMysqlModel
from rest_framework.views import APIView

# from serializers import firstSerializer

# class UserViewSet(viewsets.ModelViewSet):
#
# 	queryset=firstMysqlModel.objects.all()
# 	# print(queryset[1])
# 	serializer_class=firstSerializer
#
# 	def list(self,request):
# 		# t=request.data
# 		# p1=
# 		# print(t)
# 		# if request.method=='POST':
# 			# return Response("postpostpost")
# 		return Response("hello")

	# def a():
	# 	return Response("hello")
#
#
# class GroupViewSet(viewsets.ModelViewSet):
# 	queryset=Group.objects.all()
# 	serializer_class=GroupSerializer

class FirstAPIView(APIView):

	permissions_classes=(permissions.AllowAny,)
	authentication_classes = (authentication.TokenAuthentication,)

	def post(self,request):
		# body=json.load(request.body)
		return Response("test")