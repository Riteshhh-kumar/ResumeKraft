from django.shortcuts import render
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request,'indexnew.html')

def faq(request):
    return render(request,'faq.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def feedback(request):
    return render(request,'feedback.html')



def register(request):
    if request.user.is_authenticated:
        return render(request,"index.html")

    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        mail = request.POST.get("email")
        pasworrd = request.POST.get("password")

        try:    
            user = User.objects.create_user(username=mail,
                                                    email=mail,
                                                    password=pasworrd
                                                    )
            user.last_name=lname
            user.first_name=fname
            user.save()
            login(request,user)
            return render(request,"details.html")
        except:
            messages.error(request,"Email already registered")
            return render(request,"register.html")

    return render(request,"register.html")

def loginuser(request):
    if request.method=="POST":
        usern = request.POST.get("inputEmail")
        passw = request.POST.get("inputPassword")
        user = authenticate(request, username=usern, password=passw)
        try:
            login(request,user)
            return render(request,"indexnew.html")
        except:
            messages.error(request,"Email or Password incorrect")
            return render(request,"indexnew.html")
    return render(request,"home.html")

@login_required
def logoutuser(request):
    logout(request)
    return render(request,'indexnew.html')

@login_required
def resume(request):
    return render(request,"details.html")

def test(request):
    return render(request,"testing.html")
