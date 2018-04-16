from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from .models import up,ecash

# Create your views here.
def alogin(request):
	errors=[]
	account=None
	password=None
	if request.method=='POST':
		if not request.POST.get('account'):
			errors.append('请输入银行卡号')
		else:
			account=request.POST.get('account')
		if not request.POST.get('password'):
			errors.append('请输入密码')
		else:
			password=request.POST.get('password')
		if account is not None and password is not None:
			user=authenticate(username=account,password=password)
			if user is not None:
				if user.is_active:
					login(request,user)#??????
					return redirect('/')
				else:
					errors.append('用户不可用')
			else:
				errors.append('用户名或密码错误')
	return render(request,'account/login.html',{'errors':errors})

def register(request):
	errors=[]
	account=None
	password=None
	password2=None
	email=None
	CompareFlag=False

	if request.method=='POST':
		if not request.POST.get('account'):
			errors.append('请输入银行卡号')
		else:
			account=request.POST.get('account')
			filterResult=User.objects.filter(username=account)
			if len(filterResult)>0:
				errors.append('银行卡号已存在')
		if not request.POST.get('password'):
			errors.append('请输入密码')
		else:
			password=request.POST.get('password')
		if not request.POST.get('password2'):
			errors.append('请再次输入密码')
		else:
			password2=request.POST.get('password2')
		if not request.POST.get('email'):
			errors.append('请输入邮箱')
		else:
			email=request.POST.get('email')

		if password is not None and password2 is not None:
			if password==password2:
				CompareFlag=True
			else:
				errors.append('两次输入密码不一致')
		if account is not None and password is not None and password2 is not None and email is not None and CompareFlag:
			user=User.objects.create_user(account,email,password)
			user.is_active=True
			user.save()
			up.objects.create(user=user)
			ecash.objects.create(user=user)

			return redirect('/account/login')
	return render(request,'account/register.html',{'errors':errors})

def alogout(request):
	logout(request)
	return redirect('/account/login')
