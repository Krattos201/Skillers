from django.shortcuts import render, redirect,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from .models import person
import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox


m=tk.Tk()
wid=20
hit=10
widscr=m.winfo_screenwidth()
hitscr=m.winfo_screenheight()
x=(widscr/2)-(wid/2)
y=(hitscr/2)-(hit/2)
m.geometry("%dx%d+%d+%d" % (wid,hit,x,y))
m.after(25,lambda:m.destroy())
fname=""
lname=""
mobile=""
x=0 #global random generator
def Register_form(request):
    from pages.namer import otp
    global fname
    global lname
    global mobile
    fname= request.POST["fname"]
    lname= request.POST["lname"]
    mobile= request.POST["mobile"]
    already_present=person.objects.filter(mobile_number=mobile)
    if(already_present):
        messagebox.showinfo("WARNING!","Mobile No. already present!!!")
        return render(request,"about.html",{})
    global x
    x=random.randrange(0,999999,1)	
    return render(request, "Enter_otp.html",{"my_stuff": otp('yjsu8rb4zqI-DKidd3kCbVpIDLgTMVOBCgHP6ZrO1e', mobile,
    'TXTLCL', x)})
    
def Otp_validation(request):
    from pages.namer import dataset_generator
    otp_valid= request.POST["otp_valid"]
    if(otp_valid==x):
        y=fname+str(random.randrange(0,999999,1))
        messagebox.showinfo("SUCCESS!","Your user-id is "+ y +". Please make a note of it as this will be used in future for logging in. ")
        p=person(first_name=fname,last_name=lname,mobile_number=mobile,user_id=y)
        p.save()      
        return render(request,"home.html",{"generate": dataset_generator(mobile)})
    else:
        messagebox.showinfo("WARNING!","Wrong OTP entered!!!")
        return render(request,"about.html",{})
    
         

def home(request):
    from pages.namer import face_detector,otp
    id_f= request.POST["id"] 
    per=person.objects.filter(user_id=id_f)
    if(per):
        mob_id=face_detector()
        if(mob_id!="0"):
            if(per.mobile==mob_id):
                messagebox.showinfo("Success!","Face detection successful!!!")
                return render(request, "Enter_otp1.html",{"my_stuff": otp('yjsu8rb4zqI-DKidd3kCbVpIDLgTMVOBCgHP6ZrO1e', mobile,
                'TXTLCL', x)})
            else:
                messagebox.showinfo("WARNING!","Face not matched!!!. Try again...")
                return render(request, "home.html",{})
        else:
            messagebox.showinfo("WARNING!","Face not matched!!!. Try again...")
            return render(request, "home.html",{})    
    else:
        messagebox.showinfo("WARNING!","Enter correct User-id!!!")
        return render(request, "home.html",{})   
        

def about(request):
	return render(request,"about.html",{})

def Enter_otp(request):
	return render(request,"Enter_otp.html",{})

def Enter_otp1(request):
	return render(request,"Enter_otp1.html",{})
m.mainloop()