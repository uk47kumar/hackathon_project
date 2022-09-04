import math
import random
import smtplib

from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from TinyCoder.models import Contact
from TinyCoder.models import LOGIN
from TinyCoder.models import SIGNUP
from TinyCoder.models import APPOINTMENT
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
# Create your views here.

#


# def Login(request):
#     return render(request, 'Login.html')


def Login(request):
    user = SIGNUP.objects.all()
    email = request.POST.get('email')
    password = request.POST.get('password')

    for i in user:
        if(i.email == email and i.password == password):
            return render(request, 'Article_main.html')
    return render(request, 'Login.html')




# def Log(request):
#     if request.method == "POST":
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         data = LOGIN(email=email, password=password)
#         data.save()
#     return render(request, 'Article_main.html')


def index(request):
    allData=SIGNUP.objects.all()
    context={'datas':allData}
    return render(request, 'Article_Login.html',context)


def Article_Login(request):
    allData=SIGNUP.objects.all()
    context={'datas':allData}
    return render(request, 'Article_Login.html',context)


def saveEnquiry(request):
    if request.method == "POST":
        message = request.POST.get('message')
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        data = Contact(name=name, email=email, message=message,
                       subject=subject, date=datetime.today())
        data.save()
    return render(request, 'Article_Login.html')


def Article_main(request):
    allData=SIGNUP.objects.all()
    context={'datas':allData}
    return render(request, 'Article_main.html',context)


def contactEnquiry(request):
    if request.method == "POST":
        message = request.POST.get('message')
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        data = Contact(name=name, email=email, message=message,
                       subject=subject, date=datetime.today())
        data.save()
    return render(request, 'Article_main.html')


# def Signup(request):
#     return render(request, 'Signup.html')


def Signup(request):
    user = SIGNUP.objects.all()

    #generate otp
    digits="0123456789"
    OTP=""
    for i in range(6):
        OTP+=digits[math.floor(random.random()*10)]
    otp = OTP
    msg= "Your OTP for MADPHARM is " + otp 
    em = request.POST.get('email')
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()

    s.login("coderstiny65@gmail.com", "sgqjzwfwfvfxcvux")
    print(em)
    if(em != None):
        print(em)
        s.sendmail('otp verification',em,msg)


    usercount = 0
    p=""
    q=""
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmedpassword = request.POST.get('confirmedpassword')
        for i in user:
            if(email==i.email):
                usercount+=1
                q="user "+request.POST.get('email')+" already exists.."
        if(usercount == 0):
            data = SIGNUP(name=name, email=email, password=password, confirmedpassword = confirmedpassword, otp = otp)
            data.save()
            return redirect("/enterotp")
            p ="SignUp successfull! Login to access your account..."
    params = {"signup_Success": p, "userAreadyExists": q}
    return render(request, 'Signup.html', params)
    # return redirect('Login', params)


def appointment(request):
    return render(request, 'appointment.html')


def Appointment(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phonenumber = request.POST.get('phonenumber')
        drname = request.POST.get('drname')
        department = request.POST.get('department')
        email = request.POST.get('email')
        message = request.POST.get('message')
        data = APPOINTMENT(name=name, phonenumber=phonenumber, drname=drname,
                           department=department, email=email, message=message)
        data.save()
    return render(request, 'Article_main.html')


# def logoutUser(request):
#     logout(request)
#     return render("/Article_Login")

def otpvalidation(request):
    otp = request.POST.get('otp')
    otp_got = True
    print(otp)
    
    if(otp !=0 ):
        try: 
            otpgot = SIGNUP.objects.get(otp=otp)
            print(otpgot)
            otpgot.otp = 0 
            otpgot.save()
            print(otpgot)
    
    
        except:
            otp_got =False

    if(otp_got == True):
        return redirect("/Article_main") 
    print(otp_got)
    
    
    return render(request, 'otp.html')