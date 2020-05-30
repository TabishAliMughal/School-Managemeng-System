from django.shortcuts import render , get_object_or_404 , HttpResponseRedirect ,redirect , get_list_or_404
from .models import *
from .forms import *
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from authentication.user_handeling import unauthenticated_user, allowed_users, admin_only
import csv, io
from django.contrib import messages
from static.renderer import PdfMaker
from django.http import HttpResponse



def ManageGrListView(ListView):
    if ListView.method == 'POST':
        InClasses = ListView.POST.get('class')
        InSection = ListView.POST.get('section')
        section = Section.objects.all()
        classes = Class.objects.all()
        if InClasses == '' and InSection == '':
            lis = Gr.objects.all()
        elif InSection == '':
            lis = get_list_or_404(Gr , current_class = InClasses)
            in_ = get_object_or_404(Class, class_code = InClasses)
            InSection = 'All'
            InClasses = in_
        elif InClasses == '':
            lis = get_list_or_404(Gr , section = InSection)
            in_ = get_object_or_404(Section, sect_code = InSection)
            InClasses = 'All'
            InSection = in_
        else:
            lis = get_list_or_404(Gr , section = InSection , current_class = InClasses)
        context = {
            'one' : InClasses,
            'two' : InSection ,
            'GrNumber' : lis,
            'class' : classes,
            'section' : section,
            }
        return render (ListView,'Student/list.html',context)
    else:
        section = Section.objects.all()
        classes = Class.objects.all()
        GrNumber = Gr.objects.all()
        context = {
            'GrNumber':GrNumber,
            'class' : classes,
            'section' : section,
            'one' : 'All',
            'two' : 'All',
        }
        return render (ListView,'Student/list.html',context)

def ManageGrDetailView(DetailView,gr_number):
    GrNumber = get_object_or_404(Gr,gr_number = gr_number)
    context = {
        'GrNumber' : GrNumber,
    }
    return render (DetailView, 'Student/detail.html',context)
  
# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def ManageGrDataDownloadView(DownloadView):
    abc = HttpResponse(content_type = 'csv')
    filename = 'attachment; filename="{0}"'.format('Student Information.csv')
    abc['Content-Disposition'] = filename
    fields = (
        'gr_number' ,
        'name' ,
        'family_code' ,
        'section' ,
        'fee_concession_code' ,
        'class_of_admission' ,
        'session_of_admission' ,
        'current_class' ,
        'current_session' ,
        'admission_date' ,
        'last_school' ,
        'religion' ,
        'date_of_birth' ,
        'active' ,
    )
    data = Gr.objects.values(*fields)
    writer = csv.DictWriter(abc , fieldnames = fields)
    writer.writeheader()
    for i in data:
        writer.writerow(i)
    return abc

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def ManageGrCreateView(CreateView , query=None):
    if CreateView.method == 'POST':
        user_form = EntryForm(CreateView.POST)
        if user_form.is_valid():
            form = user_form.save()
            context = {
                'return': 'Has Been Added SuccessFully'
            }
            return render(CreateView,'Student/Create/created.html',context)
        else:
            context = {
                'return': 'Is Not Valid'
            }
            return render(CreateView,'Student/Create/created.html',context)
    if query:
        form = CreateView.GET
        query = get_object_or_404(Entry_data , pk = int(form.get('query_code')) )
        data = Entry_data.objects.all()
        user_form = EntryForm({'query_code':query,'name':query.Name,'fee_concession_code': query.Fee_type,'last_school':query.Previous_school , 'class_of_admission' : query.Suggested_class })
        Previous_school = 'selected="{}"'.format(query.Previous_school.pk)
        grnum = []
        for i in Gr.objects.all():
            grnum.append(i.gr_number)
        gr=""
        for i in grnum:
            gr = int(max(grnum) + 1)
        abc = '123'
        context = {
            'user_form':user_form ,
            'gr' : gr ,
            'data' : data ,
            'query':query ,
            'Previous_school':Previous_school ,
            'abc' : abc ,
        }
        return render(CreateView,'Student/Create/create.html',context)
    else:
        grnum = []
        for i in Gr.objects.all():
            grnum.append(i.gr_number)
        gr=""
        for i in grnum:
            gr = int(max(grnum) + 1)
        data = Entry_data.objects.all()
        user_form = EntryForm()
        context = {
            'user_form':user_form ,
            'gr' : gr ,
            'data' : data ,
        }
        return render(CreateView,'Student/Create/create.html',context)

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def ManageGrEditView(request, gr_number):
    data = get_object_or_404(Gr, gr_number = gr_number)
    if request.method == "POST":
        user_form = EntryForm(request.POST or None, instance=data)
        if user_form.is_valid():
            user_form.save()
            return redirect('gr_list')
    else:
        user_form = EntryForm(instance=data)
        return render(request, 'Student/Edit/edit.html',{'GrNumber':user_form,'data':data}) 

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def ManageGrDeleteView(request, gr_number):
    Gr.objects.filter(gr_number=gr_number).delete()
    a = Gr.objects.all()
    return render(request, 'Student/Delete/delete.html')

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def ManageGrBulkSampleDownloadView(DownloadView):
    abc = HttpResponse(content_type = 'csv')
    filename = 'attachment; filename="{0}"'.format('Gr Model Format.csv')
    abc['Content-Disposition'] = filename
    fields = (
        'gr_number' ,
        'name' ,
        'family_code' ,
        'section' ,
        'fee_concession_code' ,
        'class_of_admission' ,
        'session_of_admission' ,
        'current_class' ,
        'current_session' ,
        'admission_date' ,
        'last_school' ,
        'religion' ,
        'date_of_birth' ,
        'active' ,
    )
    # data = Gr.objects.values(*fields)
    writer = csv.DictWriter(abc , fieldnames = fields)
    writer.writeheader()
    # for i in data:
    #     writer.writerow(i)
    return abc

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def ManageGrUploadView(CreateView):
    if CreateView.method == "GET":
        return render(CreateView,"Student/Create/ViaFile/create.html")
    InFile = CreateView.FILES['file']
    if not InFile.name.endswith('.csv'):
        messages.error(CreateView, 'This is not a csv file')
    data_set = InFile.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        created = EntryForm({
            'gr_number' : column[0] ,
            'query_code' : column[1] ,
            'name' : column[2] ,
            'picture' : column[3] ,
            'family_code' : column[4] ,
            'section' : column[5] ,
            'fee_concession_code' : column[6] ,
            'class_of_admission' : column[7] ,
            'session_of_admission' : column[8] ,
            'current_class' : column[9] ,
            'current_session' : column[10] ,
            'admission_date' : column[11] ,
            'last_school' : column[12] ,
            'religion' : column[13] ,
            'date_of_birth' : column[14],
            'active' : column[15],
            })
        created.save()
    context = {}
    return render(CreateView,"Student/Create/ViaFile/create.html", context)

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def ManageGrPrintPdfView(PrintView,clas,sect):
    if PrintView.method == 'POST':
        Class_ = get_object_or_404(Class , class_name = clas)
        Sect = get_object_or_404(Section , sect_name = sect)
        lis = get_list_or_404(Gr , current_class = Class_.class_code , section = Sect.sect_code)
        context = {
            'abc' : lis ,
            'one' : clas ,
            'two' : sect ,
        }
        pdf = PdfMaker('Student/Print/print.html', context)
        return HttpResponse(pdf, content_type='application/pdf')