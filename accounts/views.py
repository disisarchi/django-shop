from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from shop.forms import RegisterForm

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/shop')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {'form': form})
