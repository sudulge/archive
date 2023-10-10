from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from common.forms import UserFrom

# Create your views here.

def signup(request):
    if request.method == "POST":
        form = UserFrom(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('movie_index')
    else:
        form = UserFrom()
    return render(request, 'common/signup.html', {'form': form})