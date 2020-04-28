from django.shortcuts import render , get_object_or_404 ,redirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from authentication.user_handeling import unauthenticated_user, allowed_users, admin_only

def ManageMainScreenView(request):
    return render(request, 'Main/Index.html')

def ManageLoginFormView(request):
    return render(request,'Main/LoginPage.html')

def ManageAboutView(request):
    return render(request,'Main/About.html')

def ManageSchoolView(request):
    return render(request,'Main/Schools.html')

def ManageContactView(request):
    return render(request,'Main/Contact.html')

def ManageTeamView(request):
    return render(request,'Main/Team.html')

def ManageDetailView(request):
    return render(request,'Main/Detail.html')

def ManageAfterLoginView(request):
    return render(request,'Admin/Common.html')

@login_required(login_url='login_url')
@allowed_users(allowed_roles=['Admin','Accountant'])
def ManageUserTypeListView(ListView):
    usertype = UserType.objects.all()
    context = {
        'usertype':usertype
    }
    return render (ListView,'User/UserType/List.html', context)

@login_required(login_url='login_url')
@allowed_users(allowed_roles=['Admin','Accountant'])
def ManageUserTypeCreateView(CreateView):
    if CreateView.method == 'POST':
        user_form = UserTypeForm(CreateView.POST)
        if user_form.is_valid():
            form = user_form.save()
            context = {
                'return': 'Has Been Added SuccessFully'
            }
            return render(CreateView,'User/UserType/Created.html', context)
        else:
            context = {
                'return': 'Is Not Valid'
            }
            return render(CreateView,'User/UserType/Created.html', context)
    else:
        user_form = UserTypeForm()
        context = {
                'form' : user_form
            }
        return render(CreateView,'User/UserType/Create.html', context)

@login_required(login_url='login_url')
@allowed_users(allowed_roles=['Admin','Accountant'])
def ManageUserTypeEditView(request, TypeCode):
    data = get_object_or_404(UserType, TypeCode = TypeCode)
    if request.method == "POST":
        user_form = UserTypeForm(request.POST or None, instance=data)
        if user_form.is_valid():
            user_form.save()
            return redirect('usertype_url')
    else:
        user_form = UserTypeForm(instance=data)
        return render(request, 'User/UserType/Edit.html',{'return':user_form,'data':data}) 

@login_required(login_url='login_url')
@allowed_users(allowed_roles=['Admin','Accountant'])
def ManageUserProfileListView(ListView):
    userprofile = UserProfile.objects.all()
    context = {
        'userprofile':userprofile
    }
    return render (ListView,'User/UserProfile/List.html',context)

@login_required(login_url='login_url')
@allowed_users(allowed_roles=['Admin','Accountant'])
def ManageUserProfileDetailView(DetailView,UserCode):
    userprofile = get_object_or_404(UserProfile,UserCode = UserCode)
    context = {
        'userprofile':userprofile
    }
    return render (DetailView,'User/UserProfile/Detail.html',context)

@login_required(login_url='login_url')
@allowed_users(allowed_roles=['Admin','Accountant'])
def ManageUserProfileCreateView(CreateView):
    if CreateView.method == 'POST':
        user_form = UserProfileForm(CreateView.POST)
        if user_form.is_valid():
            form = user_form.save()
            context = {
                'return': 'Has Been Added SuccessFully'
            }
            return render(CreateView,'User/UserProfile/Created.html',context)
        else:
            context = {
                'return': 'Is Not Valid'
            }
            return render(CreateView,'User/UserProfile/Created.html',context)
    else:
        user_form = UserProfileForm()
        context = {
                'form' : user_form
            }
        return render(CreateView,'User/UserProfile/Create.html',context)

@login_required(login_url='login_url')
@allowed_users(allowed_roles=['Admin','Accountant'])
def ManageUserProfileEditView(request, UserCode):
    data = get_object_or_404(UserProfile, UserCode = UserCode)
    if request.method == "POST":
        user_form = UserTypeForm(request.POST or None, instance=data)
        if user_form.is_valid():
            user_form.save()
            return redirect('userprofile_url')
    else:
        user_form = UserProfileForm(instance=data)
        return render(request, 'User/UserProfile/edit.html',{'return':user_form,'data':data}) 