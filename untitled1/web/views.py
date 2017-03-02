from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from .models import user


def homepage(request):
    return render(request, "homepage.html")


@csrf_exempt

def signup_attempt(request):
    if user.objects.filter(useremail=request.POST['email']).exists():
        errormessage = {"error":"A user already exists with the given email"}
        return render(request, "signuppage.html", errormessage)
    elif user.objects.filter(username=request.POST['user']).exists():
        errormessage = {"error":"Username already exists"}
        return render(request, "signuppage.html", errormessage)
    else:
        newuser = user.objects.create(first_name=request.POST["fname"], last_name=request.POST["lname"],useremail=request.POST["email"], username=request.POST["user"],password=request.POST["passw"])
        if len(newuser.username) < 5 or len(user.username) > 32:
            errormessage = {"error": "Username must be 5-32 characters"}
            return render(request, "signuppage.html", errormessage)
        elif len(newuser.password) < 5 or len(user.password) > 32:
            errormessage = {"error": "Password must be 5-32 characters"}
            return render(request, "signuppage.html", errormessage)
        newuser.save()
        return render(request, "homepage.html")

def signin_attempt(request):
    if user.objects.filter(username=request.POST['user']).exists():
        newuser = user.objects.filter(username=request.POST['user']).get()
        if request.POST['passw'] == newuser.password:
            return render(request, "homepage.html")
        else:
            errormessage = {"error": "Your Password is incorrect"}
            return render(request, "signinpage.html", errormessage)
    else:
        errormessage = {"error": "Your Username is incorrect"}
        return render(request, "signinpage.html", errormessage)


def signinpage(request):
    return render(request, "signinpage.html")

def signuppage(request):
    return render(request, "signuppage.html")