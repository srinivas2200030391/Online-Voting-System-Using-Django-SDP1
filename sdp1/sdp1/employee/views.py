import time
import random

from django.shortcuts import render
from .models import Employee, Voter, Contender, votervotemapping, Count
from django.db.models import Q
from django.http import HttpResponse
from random import *
from django.core.mail import *


# Create your views here.
def checkuser(request):
    empuname = request.POST.get("empvotid")
    emppwd = request.POST.get("pwd")
    if empuname=="" or emppwd=="":
        return render(request,"login.html")
    flag = Employee.objects.filter(Q(emp_id=empuname) & Q(password=emppwd))
    print(flag)
    if flag:
        request.session["auname"] = empuname
        now = time.localtime()
        current_time = time.strftime("%H:%M:%S")
        request.session["time"]=now
        print(request.session["time"])
        empdata = Voter.objects.all()
        h = Voter.objects.count()
        g = votervotemapping.objects.count()
        return render(request, "dashboard1.html", {"empdata": empdata, "h": h, "g": g})
    else:
        flag1 = Voter.objects.filter(Q(voter_id=empuname) & Q(password=emppwd))
        if flag1:
            empdata = Contender.objects.all()
            count = Contender.objects.count()
            request.session["auname"] = empuname
            now = time.localtime()
            current_time = time.strftime("%H:%M:%S")
            request.session["time"] = now
            print(request.session["time"])
            return render(request, "dashboard.html", {"empdata": empdata, "h": count})
        else:
            return HttpResponse("HEY")


def addvoter(request):
    flag = Voter.objects.all()
    count = Voter.objects.all().count()
    a = []
    print(flag)
    for i in flag:
        a.append(i.voter_id)
    while True:
        emp = randint(1, 100000)
        if emp not in a:
            break
    fn = request.POST['fn']
    ln = request.POST['ln']
    ftn = request.POST['ftn']
    mtn = request.POST['mtn']
    dob = request.POST['dob']
    gen = request.POST['gen']
    pw = request.POST['pwd']
    ad = request.POST['aad']
    str = request.POST['street']
    ph = request.POST['ph']
    aph = request.POST['aph']
    zip = request.POST['zip']
    cty = request.POST['city']
    con = request.POST['con']
    emai = request.POST['email']
    vot = Voter(id=count + 1, voter_id=emp, first_name=fn, last_name=ln, father_name=ftn, mother_name=mtn, year=dob,
                gender=gen, password=pw, aadhar=ad, Street=str, contact=ph, alter_contacts=aph, zip=zip, city=cty,
                country=con, email=emai)
    Voter.save(vot)

    empdata = Voter.objects.all()
    return render(request, "dashboard1.html", {"empdata": empdata})


def addvo1(request):
    return render(request, "registration.html")


def dash(request):
    auname = request.session['auname']
    st = ""
    flag = votervotemapping.objects.all()
    a = []
    for i in flag:
        a.append(i.email)
    flag = Voter.objects.all()
    for i in flag:
        if i.voter_id == int(auname):
            st += i.email
    if st == "":
        flag = Employee.objects.all()
        for i in flag:
            if i.emp_id == int(auname):
                st += i.email
    if st not in a:
        return render(request, "dash.html")
    else:
        return render(request, "thank.html")


def delvot1(request):
    pass


def forgot(request):
    return render(request, "forgotpassword.html")


def generate_otp():
    return str(randint(1000, 9999))


otp_storage = {}


def send_otp(request):
    email = request.POST['email']
    otp = generate_otp()
    otp_storage['email'] = otp
    subject = 'OTP verification'
    message = f'Your OTP for login is : {otp}'
    from_email = 'vasus4990@gmail.com'
    recipient_email = [email]
    send_mail(subject, message, from_email, recipient_email)
    return render(request, 'validate_otp.html')


def contactus(request):
    name = request.POST['na']
    email = request.POST['email']
    msg = request.POST['msg']
    to_mail = ["vasus4990@gmail.com"]
    print(email)
    send_mail(name, msg, email, to_mail)
    return render(request, 'index.html')


def validate_otp(request):
    email = request.POST['otp']
    user_otp = request.POST['otp']
    stored_otp = otp_storage.get('email')
    if user_otp == stored_otp:
        return render(request, 'changepw.html')
    else:
        print(user_otp, stored_otp)
        return HttpResponse("None")


def check_pw(request):
    auname = request.POST['uname']
    npwd = request.POST['pwd']
    a = Employee.objects.all()
    b = []
    for i in a:
        b.append(i.email)
    if auname in b:
        Employee.objects.filter(email=auname).update(password=npwd)
        return render(request, 'login.html')
    a = Voter.objects.all()
    b = []
    for i in a:
        b.append(i.email)
    if auname in b:
        Voter.objects.filter(email=auname).update(password=npwd)
        return render(request, 'login.html')


def logout(request):
    return render(request, 'index.html')


def update(request):
    a = request.POST['card']
    print(a)
    return HttpResponse("HY")


def dashb(request):
    return render(request, 'dashboard.html')


def dashb1(request):
    empdata = Voter.objects.all()
    h = Voter.objects.count()
    g = votervotemapping.objects.count()
    return render(request, "dashboard1.html", {"empdata": empdata, 'h': h, 'g': g})


def votepk(request):
    auname = request.session['auname']
    st = ""
    flag = Voter.objects.all()
    for i in flag:
        if i.voter_id == int(auname):
            st += i.email
    if st == "":
        flag = Employee.objects.all()
        for i in flag:
            if i.emp_id == int(auname):
                st += i.email
    v = votervotemapping(email=st)
    votervotemapping.save(v)
    flag=Count.objects.all()
    count=0
    for i in flag:
        if i.name=="Konidela Pawan Kalyan Babu":
            count=i.count
    count+=1
    Count.objects.filter(name="Konidela Pawan Kalyan Babu").update(count=count)
    return render(request, "thank.html")


def vote(request):
    auname = request.session['auname']
    st = ""
    flag = Voter.objects.all()
    for i in flag:
        if i.voter_id == int(auname):
            st += i.email
    if st == "":
        flag = Employee.objects.all()
        for i in flag:
            if i.emp_id == int(auname):
                st += i.email
    v = votervotemapping(email=st)
    votervotemapping.save(v)
    flag=Count.objects.all()
    count=0
    for i in flag:
        if i.name=="Nara Chandra Babu Naidu":
            count=i.count
    count+=1
    Count.objects.filter(name="Nara Chandra Babu Naidu").update(count=count)
    return render(request, "thank.html")


def votejag(request):
    auname = request.session['auname']
    st = ""
    flag = Voter.objects.all()
    for i in flag:
        if i.voter_id == int(auname):
            st += i.email
    if st == "":
        flag = Employee.objects.all()
        for i in flag:
            if i.emp_id == int(auname):
                st += i.email
    v = votervotemapping(email=st)
    votervotemapping.save(v)
    flag = Count.objects.all()
    count = 0
    for i in flag:
        if i.name == "Yeduguri Sandinti Jaganmohan Reddy":
            count = i.count
    count += 1
    Count.objects.filter(name="Yeduguri Sandinti Jaganmohan Reddy").update(count=count)
    return render(request, "thank.html")


def dash2(request):
    auname = request.session['auname']
    st = ""
    flag = votervotemapping.objects.all()
    a = []
    for i in flag:
        a.append(i.email)
    flag = Employee.objects.all()
    for i in flag:
        if i.emp_id == int(auname):
            st += i.email
    if st not in a:
        return render(request, "voter.html")
    else:
        return render(request, "thank2.html")


def dashboardvoter(request):
    empdata = Contender.objects.all()
    count = Contender.objects.count()
    return render(request, "dashboard.html", {"empdata": empdata, "h": count})


def calender(request):
    return render(request, "calender.html")


def countvote(request):
    pass
