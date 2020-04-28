from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.

def homeWork_listWise(request):
    homeWork_list = home_work.objects.all()
    log = {'Entry': homeWork_list}
    return render (request,'home_work/Create/list.html', log)

#simple add function
# def homeWork_add(request):
#     form = home_work_form(request.POST or None)
#     if form.is_valid():
#         form.save()

#     context = {
#         'form': form
#     } 
#     return render(request,'home_work/Create/add.html', context)

def homeWork_add(CreateView):
    if CreateView.method == 'POST':
        user_form = home_work_form(CreateView.POST)
        
        if user_form.is_valid():
            form = user_form.save()
            context = {
                'return': 'Has Been Added SuccessFully'
            }
            return render(CreateView,'home_work/Create/added.html',context)
        else:
            context = {
                'return': 'Is Not Valid'
            } 
            return render(CreateView,'home_work/Create/added.html',context)

    else:
        user_form = home_work_form()
        return render(CreateView,'home_work/Create/add.html',{'form':user_form})


def homeWork_update(request , homework_ID):
    data = get_object_or_404(home_work, homework_ID = homework_ID)
    if request.method == "POST":
        user_form = home_work_form(request.POST or None, instance=data)
        if user_form.is_valid():
            user_form.save()
            return redirect('home_work_listWise')
    else:
        user_form = home_work_form(instance=data)
        log = {'user':user_form,'data':data}
        return render(request, 'home_work/Create/update.html', log)


def homeWork_delete(request, homework_ID):
    home_work.objects.filter(homework_ID=homework_ID).delete()
    homeWork_delete = home_work.objects.all()
 
    log = {
        'Entry' : homeWork_delete
    }
    return render(request, 'home_work/Create/list.html', log)




