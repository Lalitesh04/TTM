from django.core.mail import send_mail
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Admin, Register, Packages


def checkadminlogin(request):
    if request.method == 'POST':
        uname = request.POST["uname"]
        passw = request.POST["pass"]
        admin = Admin.objects.filter(Q(username=uname) & Q(password=passw))
        user = Register.objects.filter(Q(uname=uname) & Q(password=passw))
        if admin:
            return render(request, "adminhome.html")
        elif user:
            return render(request, "userhome.html")
        else:
            message = "Invalid Login"
            return render(request, "login.html", {"message": message})


def checkregistration(request):
    if request.method == 'POST':
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        uname = request.POST["uname"]
        password = request.POST["password"]
        cpassword = request.POST["cpassword"]
        if password != cpassword:
            return render(request, 'Register.html', {'error_message': 'Passwords do not match'})
        new_registration = Register(name=name, email=email, phone_number=phone, uname=uname, password=password)
        new_registration.save()
        message = "Registered SuccessFully"
        return render(request, "login.html", {'message': message})


def userhome(request):
    return render(request, "userhome.html")


def adminhome(request):
    return render(request, "adminhome.html")


def addpackage(request):
    return render(request, "addpackage.html")


def checkpackage(request):
    if request.method == "POST":
        tcode = request.POST["tourcode"]
        tname = request.POST["tourname"]
        tpackage = request.POST["tourpackage"]
        tdesc = request.POST["desc"]
        new_package = Packages(tourcode=tcode, tourname=tname, tourpackage=tpackage, desc=tdesc)
        new_package.save()
        messages.info(request, "Package Added SuccessFully")
        return redirect(addpackage)


def viewpackage(request):
    count = Packages.objects.count()
    package = Packages.objects.all().order_by('tourcode').values()
    return render(request, "viewpackage.html", {"package": package, "count": count})


def userpackage(request):
    count = Packages.objects.count()
    package = Packages.objects.all().order_by('tourcode').values()
    return render(request, "userpackage.html", {"package": package, "count": count})


def changepassword(request):
    if request.method == "POST":
        uname = request.POST["uname"]
        opwd = request.POST["opwd"]
        npwd = request.POST["npwd"]
        flag = Register.objects.filter(userhome=uname, password=opwd).values()
        if flag:
            Register.objects.filter(userhome=uname, password=opwd).update(password=npwd)
            return render(request, "index.html")

        else:
            return render(request, "changepassword.html")


def mail(request):
    return render(request, "sendmail.html")


def mailsend(request):
    if request.method == "POST":
        email = request.POST["email"]
        subject = request.POST["subject"]
        body = request.POST["body"]
        send_mail(subject, body, "lalitesh.mupparaju04@gmail.com",[email],fail_silently=False)
        messages.info(request,"Mail Sent SuccessFully")
        return redirect('mail')
    else:
        return redirect('mail')
