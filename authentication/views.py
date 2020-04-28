from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .user_handeling import unauthenticated_user, allowed_users, admin_only
from .forms import *

@unauthenticated_user
def registerPage(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			group = Group.objects.get(name='customer')
			user.groups.add(group)
			messages.success(request, 'Account was created for ' + username)
			return redirect('')
	context = {
        'form':form
        }
	return render(request, 'Authentication/register.html', context)

@unauthenticated_user
def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('after_login_url')
		else:
			messages.info(request, 'Username OR password is incorrect')
	context = {}
	return render(request, 'Main/LoginPage.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login_url')

# @admin_only
# @login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])