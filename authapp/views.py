from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages




# Create your views here.
def signup(request):
    if request.method == 'POST':
        get_email = request.POST['email']
        get_password1 = request.POST['pass1']
        get_password2 = request.POST['pass2']
        if get_password1 != get_password2:
            messages.info(request, 'Password is not matching')
            return redirect('/auth/signup')

        try:
            if User.objects.get(username=get_email):
                messages.warning(request, 'Email is taken')
        except Exception as identifier:
            pass
        myuser = User.objects.create_user(get_email, get_email, get_password1,)
        myuser.save()
        messages.success(request, 'User is created Please Login')
        return redirect('/auth/login')

    return render(request, 'signup.html')

def handleLogin(request):
    if request.method == 'POST':
        get_email = request.POST['email']
        get_password1 = request.POST['pass1']

        myuser = authenticate(username=get_email, password=get_password1)

        if myuser is not None:
            login(request,  myuser)
            messages.success(request, 'Login is successful')
            return redirect('/')
        else:
            messages.error(request, 'Invalid Credentials')

    return render(request, 'login.html')

def handleLogout(request):
    logout(request)
    messages.success(request, 'Logout is successful')
    return render(request, 'login.html')


