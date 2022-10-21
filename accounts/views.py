from django.shortcuts import render

# Create your views here.
from pyexpat.errors import messages
from django.shortcuts import render,redirect
from app.models import Event
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        customer = User.objects.create_user(username,email,password)
        customer.save()

        return redirect('login')

    events = Event.objects.all()
    context = {'events':events}

    return render(request, 'accounts/signup.html', context)

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            username = user.username

            return redirect('/')
        else:
            # messages.error(request, "Bad Credentials")
            return redirect('login')

    events = Event.objects.all()
    context = {'events':events}

    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('/')