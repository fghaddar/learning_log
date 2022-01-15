from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        form = UserCreationForm
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()                                      # form.save() stores username and hash password and returns the newly created user
            authenticated_user = authenticate(                          # if username and pass correct, then authenticate returns a user object 
                username = new_user.username,
                password = request.POST['password1']
            )                
            login(request, authenticated_user)                          # create a session for the user               
            return HttpResponseRedirect(
                reverse('learning_logs:index')
            )
    
    context = {'form': form}
    return render(request, 'users/register.html', context)