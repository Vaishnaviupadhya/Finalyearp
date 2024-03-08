# # views.py
from django.shortcuts import render, redirect
from home.models import CustomUser
from django.contrib.auth import login,authenticate,logout
# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, "index.html")

def braind(request):
    return render(request, "braind.html")

# def login(request):
#      if request.method == 'POST':
#         lemail = request.POST.get('lemail')
#         user_type = int(request.POST.get('roles'))  # Convert to integer
#         lpass1 = request.POST.get('lpass1')
#         print(lemail,user_type,lpass1)
#         user = authenticate(request, username=lemail, password=lpass1)
#         print
#         if user is not None:
#             # Check if the authenticated user has the correct role
#             if user.Type == user_type:
#                 # Log in the user
#                 login(request, user)
#                 return HttpResponse("Login successful!")  # You can redirect to another page if needed
#             else:
#                 return HttpResponse("Incorrect role! Please check your credentials.")
#         else:
#             return HttpResponse("Invalid login credentials. Please try again.")

#         #return redirect('signup')
#      return render(request, "index.html")
# views.py
# def login(request):
#     if request.method == 'POST':
#         lemail = request.POST.get('lemail')
#         user_type = int(request.POST.get('roles'))
#         lpass1 = request.POST.get('lpass1')
#         print(lemail, user_type, lpass1)

#         # Authenticate using email and password
#         user = authenticate(request, email=lemail, password=lpass1)
#         print(user)
#         if user is not None:
#             # Check if the authenticated user has the correct role
#             if user.type == user_type:
#                 # Log in the user
#                 login(request, user)
#                 return HttpResponse("Login successful!")
#             else:
#                 return HttpResponse("Incorrect role! Please check your credentials.")
#         else:
#             return HttpResponse("Invalid login credentials. Please try again.")

#     return render(request, "index.html")

# def signup(request):
#     if request.method == 'POST':
#         uname = request.POST.get('name')
#         uemail = request.POST.get('uemail')
#         user_type = int(request.POST.get('role'))  # Convert to integer
#         pass1 = request.POST.get('pass1')
#         pass2 = request.POST.get('pass2')
#         print(uname,uemail,user_type,pass1,pass2)
#         my_user = CustomUser.objects.create_user(username=uname, email=uemail, password=pass1, type=user_type)
#         my_user.save()
#         return redirect('login')
#     return render(request, "index.html")
# def signup(request):
#     if request.method == 'POST':
#         uname = request.POST.get('name')
#         uemail = request.POST.get('uemail')
#         user_type = int(request.POST.get('role'))
#         pass1 = request.POST.get('pass1')
#         pass2 = request.POST.get('pass2')
#         print(uname, uemail, user_type, pass1, pass2)

#         # Create the user with email instead of username
#         my_user = CustomUser.objects.create_user(uname,uemail,pass1,user_type)
#         my_user.save()

#         return redirect('login')
def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('name')
        uemail = request.POST.get('uemail')
        user_type = int(request.POST.get('role'))
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        # Create the user with email instead of username
        my_user = CustomUser.objects.create_user(email=uemail, password=pass1, name=uname, type=user_type)
        my_user.save()
        return redirect('home')

    return redirect('home')

def logins(request):
    if request.method == 'POST':
        lemail = request.POST.get('lemail')
        user_type = int(request.POST.get('roles'))
        lpass1 = request.POST.get('lpass1')
        print(lemail,user_type,lpass1)
    
        # Authenticate using email and password
        user = authenticate(request, email=lemail, password=lpass1)
        print(user)
        if user is not None:
            # Check if the authenticated user has the correct role
            if user.type == user_type:
                # Log in the user
                login(request, user)
                #return HttpResponse("Login successful!")
                if user_type == 0:  # Patient
                    return redirect('homep')
                elif user_type == 1:  # Doctor
                    return redirect('homed')
            else:
                return HttpResponse("Incorrect role! Please check your credentials.")
        else:
            return HttpResponse("Invalid login credentials. Please try again.")

    return redirect('home')

def homep(request):
    return render(request, "patient.html")

def homed(request):
    return render(request, "doctor.html")

def logoutp(request):
    logout(request)
    return redirect('home')