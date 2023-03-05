from django.shortcuts import render
from django.views import View

from app.models import User, Owner
from classes.Users.users import AbstractUser


class Login(View):
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        # Verify user information in login
        query = User.objects.filter(username=request.POST['username'], password=request.POST['password'])

        logged_user: AbstractUser = None
        if len(query) > 0:
            logged_user_model: User = query[0]
            user_type = logged_user_model.user_type
            # determine type of user instance
            if user_type == "Owner":
                logged_user = Owner(logged_user_model)
        else:
            return render(request, "login.html", {'message': "Invalid Username or Password."})

        if logged_user == None:
            return render(request, "login.html", {'message': "An unknown error has occurred."})

        # Store as logged user
        request.session["current_user_account_id"] = query[0].account_ID

        context = {}

        t = None
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type == "Owner":
            t = './homeStates/home.html'
        else:
            t = './homeStates/home.html'

        if t == None:
            return render(request, "login.html", {'message': "An unknown error has occurred."})
        else:
            return render(request, "home.html", {'HomeState': t})


class Home(View):
    def get(self, request):
        t = None
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type == "TA":
            t = './home.html'
        else:
            t = './home.html'

        if t == None:
            return render(request, "login.html", {'message': "An unknown error has occurred."})
        else:
            return render(request, "home.html", {'HomeState': t})

    def post(self, request):


        t = None
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type == "TA":
            t = './homeStates/TAHome.html'
        elif user_type == "Instructor":
            t = './homeStates/InstructorHome.html'
        elif user_type == "Admin":
            t = './homeStates/AdminHome.html'

        if t == None:
            return render(request, "login.html", {'message': "An unknown error has occurred."})
        else:
            return render(request, "home.html", {'HomeState': t})


class LogOut(View):
    def get(self, request):
        request.session["current_user_account_id"] = None
        return render(request, 'login.html', {'message': "You have been logged out of the system."})

    def post(self, request):
        # Verify user information in login
        request.session["current_user_account_id"] = None
        return render(request, 'login.html', {'message': "You have been logged out of the system."})


class AccountManagement(View):
    def get(self, request):
        t = None
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type == "Admin":
            t = './AccountManagementStates/AdminAccMng.html'

        if t == None:
            return render(request, "login.html", {'message': "An unknown error has occurred."})
        else:
            return render(request, "ManageAccount.html", {'State': t})


class CreateAccount(View):
    def get(self, request):
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type != "Admin":
            return render(request, "login.html", {'message': "An unknown error has occurred."})
        else:
            return render(request, "AccountCreate.html", {})

    def post(self, request):
        user_type = User.objects.get(account_ID=request.session['current_user_account_id']).user_type
        if user_type != "Admin":
            return render(request, "login.html", {'message': "An unknown error has occurred."})
        else:
            return render(request, "AccountCreate.html", {})
