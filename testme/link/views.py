# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def first(request):
	return render(request,'link/login.html')

def second(request):
	user_name=request.POST.get('account')
	pass_word=request.POST.get('password')
	# print(request.method)
	# return HttpResponse('{{account}}<p>this is a test</p>',content_type='text/html')
	return render(request,'link/register.html',{'user_name':user_name,'pass_word':pass_word})