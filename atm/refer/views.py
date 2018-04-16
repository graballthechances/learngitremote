from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
from account.models import up,ecash


# Create your views here.
def mainpage(request):
	i=request.user.is_authenticated()
	user=request.user
	return render(request,'refer/mainpage.html',{'user':user})

#存款
def deposit_input(request):
	errors=[]
	#如果提交
	if request.method=='POST':
		currency=request.POST.get('currency')
		if currency=='港币' or currency=='美元' or currency=='人民币':
			request.session['currency']=currency
		else:
			errors.append('请输入有效的货币：港币、人民币或是美元')
		amount=request.POST.get('amount')
		if int(amount)<100 :
			errors.append('请输入一百元以上的金额，并以百元为单位')
		request.session['currency']=currency
		request.session['amount']=amount
		if errors:
			return render(request,'refer/deposit_input.html',{'errors':errors})
		else:
			return redirect('/depositfinish/')

	return render(request,'refer/deposit_input.html',{'errors':errors})

def deposit_finish(request):
	if request.session.get('currency')=='港币':
		request.user.up.change_hk(request.user.up.hk_balance+int(request.session.get('amount')))
		request.session['amount']=0
	if request.session.get('currency')=='美元':
		request.user.up.change_dollar(request.user.up.dollar_balance+int(request.session.get('amount')))
		request.session['amount']=0
	if request.session.get('currency')=='人民币':
		request.user.up.change_yuan(request.user.up.yuan_balance+int(request.session.get('amount')))
		request.session['amount']=0

	yuan_balance=request.user.up.yuan_balance
	dollar_balance=request.user.up.dollar_balance
	hk_balance=request.user.up.hk_balance

	return render(request,'refer/deposit_finish.html',{'yuan_balance':yuan_balance,'hk_balance':hk_balance,'dollar_balance':dollar_balance})

#取款
def withdraw_input(request):
	errors=[]
	if request.method=='POST':
		currency=request.POST.get('currency')
		if currency=='港币' or currency=='美元' or currency=='人民币':
			request.session['currency']=currency
		else:
			errors.append('请输入有效的货币：港币、人民币或是美元')

		amount=request.POST.get('amount')

		if int(amount)<100 :
			errors.append('请输入一百元以上的金额，并以百元为单位')

		if currency=='港币':
			if int(amount)>request.user.up.hk_balance:
				errors.append('取款数目超出余额')
		if currency=='美元':
			if int(amount)>request.user.up.dollar_balance:
				errors.append('取款数目超出余额')
		if currency=='人民币':
			if int(amount)>request.user.up.yuan_balance:
				errors.append('取款数目超出余额')

		request.session['amount']=amount
		if errors:
			return render(request,'refer/deposit_input.html',{'errors':errors})
		else:
			return redirect('/withdrawfinish/')

	return render(request,'refer/withdraw_input.html')

def withdraw_finish(request):
	if request.session.get('currency')=='港币':
		request.user.up.change_hk(request.user.up.hk_balance-int(request.session.get('amount')))
		request.session['amount']=0
	if request.session.get('currency')=='美元':
		request.user.up.change_dollar(request.user.up.dollar_balance-int(request.session.get('amount')))
		request.session['amount']=0
	if request.session.get('currency')=='人民币':
		request.user.up.change_yuan(request.user.up.yuan_balance-int(request.session.get('amount')))
		request.session['amount']=0

	yuan_balance=request.user.up.yuan_balance
	dollar_balance=request.user.up.dollar_balance
	hk_balance=request.user.up.hk_balance

	return render(request,'refer/withdraw_finish.html',{'yuan_balance':yuan_balance,'hk_balance':hk_balance,'dollar_balance':dollar_balance})

#转账
def transfer_input(request):
	errors=[]
	if request.method=='POST':
		currency=request.POST.get('currency')
		if currency=='港币' or currency=='人民币' or currency=='美元':
			request.session['currency']=currency
		else:
			errors.append('请输入有效的货币：港币、人民币或是美元')
		amount=request.POST.get('amount')

		if int(amount)<100 :
			errors.append('请输入一百元以上的金额，并以百元为单位')

		if currency=='港币':
			if int(amount)>request.user.up.hk_balance:
				errors.append('转账数目超出余额')
		if currency=='美元':
			if int(amount)>request.user.up.dollar_balance:
				errors.append('转账数目超出余额')
		if currency=='人民币':
			if int(amount)>request.user.up.yuan_balance:
				errors.append('转账数目超出余额')

		account=request.POST.get('account')
		if User.objects.filter(username=account):
			request.session['account']=account
		else:
			errors.append('您输入的用户不存在！')
		request.session['currency']=currency
		request.session['amount']=amount
		if errors:
			return render(request,'refer/transfer_input.html',{'errors':errors})
		else:
			return redirect('/transferfinish/')
	return render(request,'refer/transfer_input.html')

def transfer_finish(request):
	account=request.session.get('account')
	user=User.objects.get(username=account)
	if request.session.get('currency')=='港币':
		request.user.up.change_hk(request.user.up.hk_balance-int(request.session.get('amount')))
		request.session['amount2']=request.session['amount']
		user.up.change_hk(user.up.hk_balance+int(request.session.get('amount')))
		request.session['amount']=0

	if request.session.get('currency')=='美元':
		request.user.up.change_dollar(request.user.up.dollar_balance-int(request.session.get('amount')))
		request.session['amount2']=request.session['amount']
		user.up.change_dollar(user.up.dollar_balance+int(request.session.get('amount')))
		request.session['amount']=0


	if request.session.get('currency')=='人民币':
		request.user.up.change_yuan(request.user.up.yuan_balance-int(request.session.get('amount')))
		request.session['amount2']=request.session['amount']
		user.up.change_yuan(user.up.yuan_balance+int(request.session.get('amount')))
		request.session['amount']=0

	yuan_balance=request.user.up.yuan_balance
	dollar_balance=request.user.up.dollar_balance
	hk_balance=request.user.up.hk_balance

	amount2=request.session.get('amount2')

	return render(request,'refer/transfer_finish.html',{'yuan_balance':yuan_balance,'hk_balance':hk_balance,'dollar_balance':dollar_balance,'account':account,'amount2':amount2})

def inquery(request):
	user=request.user
	return render(request,'refer/inquery.html',{'user':user})

def change_password(request):
	errors=[]

	if request.method=='POST':
		old_password=request.POST.get('old_password')
		new_password=request.POST.get('new_password')
		if old_password:
			t=authenticate(username=request.user.username,password=old_password)
			if t is not None:
				if t.is_active:
					if new_password:
						request.session['new_password']=new_password
						if new_password!=old_password:
							request.session['new_password']=new_password
						else:
							errors.append('新密码不能和原始密码相同！')
					else:
						errors.append('新密码不能为空')
				else:
					errors.append('请输入正确的原始密码')
			else:
				errors.append('输入的原始密码有误')
		else:
			errors.append('原始密码不能为空')


		if errors:
			return render(request,'refer/change_password.html',{'errors':errors})
		else:
			return redirect('/changefinish/')
	return render(request,'refer/change_password.html')

def change_finish(request):
	user=request.user
	user.set_password(request.session.get('new_password'))
	user.save()
	pword=request.session.get('new_password')
	# logout(request)
	return render(request,'refer/change_finish.html',{'pword':pword})

def ecash_mainpage(request):
	return render(request,'refer/ecash_mainpage.html')

def ecash_balance(request):
	user=request.user
	ecash=user.ecash.e_balance
	return render(request,'refer/ecash_balance.html',{'ecash':ecash})

def ecash_in(request):
	errors=[]
	user=request.user
	if request.method=='POST':
		amount=request.POST.get('num')
		if amount:
			if user.up.yuan_balance<int(amount):
				errors.append('您的信用卡余额不足！')
			else:
				user.up.change_yuan(user.up.yuan_balance-int(amount))
				user.ecash.change_ecash(user.ecash.e_balance+int(amount))
		else:
			errors.append('转入金额不能为空')
		if errors:
			return render(request,'refer/ecash_in.html',{'errors':errors})
		else:
			return redirect('/ecashbalance/')
	return render(request,'refer/ecash_in.html')

def ecash_out(request):
	errors=[]
	user=request.user
	if request.method=='POST':
		amount=request.POST.get('num')
		if amount:
			if user.ecash.e_balance<int(amount):
				errors.append('您的电子现金钱包余额不足！')
			else:
				user.up.change_yuan(user.up.yuan_balance+int(amount))
				user.ecash.change_ecash(user.ecash.e_balance-int(amount))
		else:
			errors.append('转出金额不能为空')
		if errors:
			return render(request,'refer/ecash_out.html',{'errors':errors})
		else:
			return redirect('/ecashbalance/')
	return render(request,'refer/ecash_out.html')
