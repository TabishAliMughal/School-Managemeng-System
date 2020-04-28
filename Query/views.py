from django.shortcuts import render,redirect, get_object_or_404, HttpResponse , get_list_or_404
from .models import Entry_data
from .forms import Form
from .filters import Query_filter
from django.contrib.auth.decorators import login_required
from authentication.user_handeling import unauthenticated_user, allowed_users, admin_only
import csv, io
from django.contrib import messages
from static.renderer import PdfMaker



def home(request):
    return render(request, 'query/entry_test.html')

def form(request):
    if request.method == 'POST':
        user_form = Form(request.POST)
        if user_form.is_valid():
            form = user_form.save()
            context = {
                'return': 'Has Been Added SuccessFully'
            }
            return render(request,'query/created.html',context)
        else:
            context = {
                'return': 'Is Not Valid'
            }
            return render(request,'query/created.html',context)
    else:
        user_form = Form()
        return render(request,'query/query_form.html',{'user_form':user_form})

def detail(request,Query_code):
    abc = get_object_or_404(Entry_data,Query_code = Query_code)
    context = {
        'Entry': abc,
    }
    return render(request, 'query/query_detail.html', context)

def list_view(request):
    Entry_dataa = Entry_data.objects.all()
    myFilter = Query_filter(request.GET, queryset=Entry_dataa)
    Entry_dataa = myFilter.qs
    context = {'Entry': Entry_dataa, 'myFilter': myFilter}
    return render(request,'query/query_list.html', context)

@login_required(login_url='login_url')
@allowed_users(allowed_roles=['Admin','Accountant'])
def edit(request,Query_code):
    i = get_object_or_404(Entry_data, Query_code=Query_code)
    if request.method == "POST":
        user_form = Form(request.POST, instance=i)
        if user_form.is_valid():
            user_form.save()
            return redirect('list_view')
    else:
        user_form = Form(instance=i)
        return render(request, 'query/edit_query.html', {'user_form':user_form})

def delete(request, Query_code):
    Entry_data.objects.filter(Query_code=Query_code).delete()
    a = Entry_data.objects.all()

    context = {
        'Entry' : a
    }
    return render(request, 'query/query_list.html', context)

def query_upload(request):
    template = "query_upload.html"

    prompt = {
        'order': 'Order by same sequence of query'
    }
    if request.method == "GET":
        return render(request,"query_upload.html",prompt)
    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        created = Form({
            'Name':column[0], 
            'father_name':column[1],
            'Address' :column[2], 
            'gender':column[3], 
            'last':column[4], 
            'Previous_school':column[5],
            'Addmission_required':column[6], 
            'Test_performed':column[7],
            'Suggested_class':column[8],
            'test_teacher':column[9],
            'date_of_test':column[10],
            'Fee_type':column[11],
            'Contact':column[12] 
        })
        print(created)
        created.save()
    context = {'abc' : 'Added Successfully'}
    return render(request, "query_upload.html", context)

def query_download(request):
    items = Entry_data.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="query.csv"'
    writer = csv.writer(response, delimiter=',')
    writer.writerow(['Name','father_name','Address','gender','last','Previous_school','Addmission_required','Test_performed','Suggested_class','test_teacher','date_of_test','Fee_type','Contact'])
    for obj in items:
        writer.writerow([obj.Name, obj.father_name, obj.Address, obj.gender, obj.last, obj.Previous_school, obj.Addmission_required, obj.Test_performed, obj.Suggested_class, obj.test_teacher, obj.date_of_test, obj.Fee_type, obj.Contact])
    return response

def query_print(request):
    data = []
    if request.method == 'POST':
        rawdata = request.POST
        Code_ = rawdata.getlist('Code' , default='1')
        for i in Code_:
            data.append(get_object_or_404(Entry_data , Query_code = i))
    context = {
        'data' : data ,
    }
    pdf = PdfMaker("query/query_print.html",context)
    return HttpResponse(pdf , content_type='application/pdf')
