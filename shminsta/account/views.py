from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)  # instantiate form with the submitted data
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])  # checks user credentials and return a user object
            if user is not None:
                if user.is_active:
                    login(request, user)  # set the user in the current session
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()  # instantiate a new log in form

    return render(request, 'account/login.html', {'form': form})


@login_required
def dashboard(request):
    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard'})
