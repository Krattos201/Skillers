from django.shortcuts import render, redirect,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from .models import person
import random
x=0 #global random generator
def Register_form(request):
	from pages.namer import otp
	fname= request.POST["fname"]
	lname= request.POST["lname"]
	mobile= request.POST["mobile"]
	p=person(first_name=fname,last_name=lname,mobile_number=mobile)
	p.save()
	global x
	x=random.randrange(0,999999,1)	
	return render(request, "about.html",{"my_stuff": otp('yjsu8rb4zqI-DKidd3kCbVpIDLgTMVOBCgHP6ZrO1e', mobile,
	'TXTLCL', x)})

def Otp_validation(request):
	otp_valid= request.POST["otp_valid"]
	return render_to_response("Enter_otp.html",message="yipppeeeeee")
	if otp_valid==2234:
		return render_to_response("Enter_otp.html",message="yipppeeeeee")
		return render(request,"home.html",{})	
	else:
		return render_to_response("Enter_otp.html",message="ghuso")

def redirect(request):
	return HttpResponseRedirect('http://localhost:8084')

def home(request):
	return render(request,"home.html",{})

def about(request):
	
	return render(request,"about.html",{})

def Enter_otp(request):
	return render(request,"Enter_otp.html",{})