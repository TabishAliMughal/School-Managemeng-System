import csv, io
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, get_list_or_404
from .models import Class, School, Family, Fee_Concession, Section, Session, Religion, Subject, Class_Subject, Fee_Type, Month, City
from .forms import class_form, school_form, family_form, fee_concession_form, section_form, session_form, religion_form, subject_form, classes_subject_form, fee_type_form, month_form, city_form
from django.contrib.auth.decorators import login_required
from authentication.user_handeling import unauthenticated_user, allowed_users, admin_only
import io, csv
from django.contrib import messages
from static.renderer import PdfMaker



# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def class_list(request):
    clas = Class.objects.all()
    context = {'Class': clas}
    return render(request, 'Dependencies/Classes/list.html', context)

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def classes(request):
    if request.method == 'POST':
        user_form = class_form(request.POST)
        if user_form.is_valid():
            classes = user_form.save()
            context = {
                'return': 'Has been added successfully'
            }
            return render(request,'Dependencies/Classes/created_classes_form.html', context)
        else:
            context = {
                'return': 'Is not valid'
            }
            return render(request,'Dependencies/Classes/created_classes_form.html', context)
    else:
        user_form = class_form()
        return render(request,'Dependencies/Classes/classes_form.html',{'user_form':user_form})


def class_upload(request):
    template = "Dependencies/Classes/class_upload.html"

    prompt = {
        'order': 'Order of the CSV should be class_code, class_name, remarks'
    }

    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Class.objects.update_or_create(
            class_code=column[0],
            class_name=column[1],
            remarks=column[2]
        )
        print(created)
    context = {'hel': 'Added Successfully'}
    return render(request, template, context)


def class_download(request):

    items = Class.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="classes.csv"'

    writer = csv.writer(response, delimiter=',')
    writer.writerow(['class_code', 'class_name', 'remarks'])

    return response
    

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def edit_class(request,class_code):
    clas = get_object_or_404(Class, class_code=class_code)
    if request.method == "POST":
        user_form = class_form(request.POST or None, instance=clas)
        if user_form.is_valid():
            user_form.save()
            return redirect('class_list')
    else:
        user_form = class_form(instance=clas)

        return render(request, 'Dependencies/Classes/editclass.html', {'user_form': user_form})

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def delete_class(request, class_code):
    Class.objects.filter(class_code=class_code).delete()
    cla = Class.objects.all()

    context = {
        'Class' : cla
    }
    return render(request, 'Dependencies/Classes/list.html', context) 




# @login_required(login_url='login_url')
def school_list(request):
    schol = School.objects.all()
    context = {'school': schol}
    return render(request, 'Dependencies/Schools/list.html', context)

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def schools(request):
    if request.method == 'POST':
        user_form = school_form(request.POST)
        if user_form.is_valid():
            schools = user_form.save()
            context = {
                'return': 'Has been added successfully'
            }
            return render(request,'Dependencies/Schools/created_schools_form.html', context)
        else:
            context = {
                'return': 'Is not valid'
            }
            return render(request,'Dependencies/Schools/created_schools_form.html', context)
    else:
        user_form = school_form()
        return render(request,'Dependencies/Schools/schools_form.html',{'user_form':user_form})


def school_upload(request):
    template = "Dependencies/Schools/school_upload.html"

    prompt = {
        'order': 'Order of the CSV should be school_code, school_name, school_area, remarks'
    }

    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = School.objects.update_or_create(
            school_code=column[0],
            school_name=column[1],
            school_area=column[2],
            remarks=column[3]
        )
    print(created)
    context = {'sch': 'Added Successfully'}
    return render(request, template, context)


def school_download(request):

    items = School.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="school.csv"'

    writer = csv.writer(response, delimiter=',')
    writer.writerow(['school_code', 'school_name', 'school_area', 'remarks'])

    return response


# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def edit_school(request, school_code):
    schol = get_object_or_404(School, school_code=school_code)

    if request.method == "POST":
        user_form = school_form(request.POST or None, instance=schol)
        if user_form.is_valid():
            user_form.save()
            return redirect('school_list')
    else:
        user_form = school_form(instance=schol)

        return render(request, 'Dependencies/Schools/editschool.html', {'user_form': user_form})

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def delete_school(request, school_code):
    School.objects.filter(school_code=school_code).delete()
    sch = School.objects.all()

    context = {
        'school' : sch
    }
    return render(request, 'Dependencies/Schools/list.html', context) 

# @login_required(login_url='login_url')
def family_list(request):
    fami = Family.objects.all()
    context = {'family': fami}
    return render(request, 'Dependencies/Family/list.html', context)

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def families(request):
    if request.method == 'POST':
        user_form = family_form(request.POST)
        if user_form.is_valid():
            families = user_form.save()
            context = {
                'return': 'Has been added successfully'
            }
            return render(request,'Dependencies/Family/created_families_form.html', context)
        else:
            context = {
                'return': 'Is not valid'
            }
            return render(request,'Dependencies/Family/created_families_form.html', context)
    else:
        user_form = family_form()
        return render(request,'Dependencies/Family/families_form.html',{'user_form':user_form})


def family_upload(request):
    template = "Dependencies/Family/family_upload.html"

    prompt = {
        'order': 'Order of the CSV should be family_code, surname, father_name, ph_no_father, mother_name, ph_no_mother, address'
    }

    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Family.objects.update_or_create(
            family_code=column[0],
            surname=column[1],
            father_name=column[2],
            ph_no_father=column[3],
            mother_name=column[4],
            ph_no_mother=column[5],
            address=column[6]
        )
    print(created)
    context = {'fam': 'Added Successfully'}
    return render(request, template, context)


def family_download(request):

    items = Family.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="families.csv"'

    writer = csv.writer(response, delimiter=',')
    writer.writerow(['family_code', 'surname', 'father_name', 'ph_no_father', 'mother_name', 'ph_no_mother', 'address'])

    return response


# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def edit_family(request, family_code):
    fami = get_object_or_404(Family, family_code=family_code)

    if request.method == "POST":
        user_form = family_form(request.POST or None, instance=fami)
        if user_form.is_valid():
            user_form.save()
            return redirect('family_list')
    else:
        user_form = family_form(instance=fami)

        return render(request, 'Dependencies/Family/editfamily.html', {'user_form': user_form})

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def family_detail(request,family_code):
    fmil = get_object_or_404(Family,family_code = family_code)
    context = {
        'family': fmil,
    }
    return render(request, 'Dependencies/Family/detail.html', context)

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def delete_family(request, family_code):
    Family.objects.filter(family_code=family_code).delete()
    famil = Family.objects.all()

    context = {
        'family' : famil
    }
    return render(request, 'Dependencies/Family/list.html', context) 

def ManageFamilyPrintPdfView(PrintView):
    fami = Family.objects.all()
    context = {
        'abc' : fami ,
    }
    pdf = PdfMaker('Dependencies/Family/print.html', context)
    return HttpResponse(pdf, content_type='application/pdf')
    # return render(PrintView,'Dependencies/Family/print.html',context)

# @login_required(login_url='login_url')
def fee_concession_list(request):
    fee = Fee_Concession.objects.all()
    context = {'fees': fee}
    return render(request, 'Dependencies/FeeConcession/list.html', context)

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def fee_concession(request):
    if request.method == 'POST':
        user_form = fee_concession_form(request.POST)
        if user_form.is_valid():
            fee_concession = user_form.save()
            context = {
                'return': 'Has been added successfully'
            }
            return render(request,'Dependencies/FeeConcession/created_fee_concession_form.html', context)
        else:
            context = {
                'return': 'Is not valid'
            }
            return render(request,'Dependencies/FeeConcession/created_fee_concession_form.html', context)
    else:
        user_form = fee_concession_form()
        return render(request,'Dependencies/FeeConcession/fee_concession_form.html',{'user_form':user_form})

def fee_concession_upload(request):
    template = "Dependencies/FeeConcession/fee_concession_upload.html"

    prompt = {
        'order': 'Order of the CSV should be fee_concession_code, fee_concession_name, concession_percent, description'
    }

    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Fee_Concession.objects.update_or_create(
            fee_concession_code=column[0],
            fee_concession_name=column[1],
            concession_percent=column[2],
            description=column[3]
        )
    print(created)
    context = {'fe': 'Added Successfully'}
    return render(request, template, context)


def fee_concession_download(request):

    items = Fee_Concession.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Fee_Concession.csv"'

    writer = csv.writer(response, delimiter=',')
    writer.writerow(['fee_concession_code', 'fee_concession_name', 'concession_percent', 'description'])

    return response

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def edit_fee_concession(request, fee_concession_code):
    fee = get_object_or_404(Fee_Concession, fee_concession_code=fee_concession_code)

    if request.method == "POST":
        user_form = fee_concession_form(request.POST or None, instance=fee)
        if user_form.is_valid():
            user_form.save()
            return redirect('fee_concession_list')
    else:
        user_form = fee_concession_form(instance=fee)

        return render(request, 'Dependencies/FeeConcession/editfee.html', {'user_form': user_form})

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def delete_fee_concession(request, fee_concession_code):
    Fee_Concession.objects.filter(fee_concession_code=fee_concession_code).delete()
    fC = Fee_Concession.objects.all()

    context = {
        'fees' : fC
    }
    return render(request, 'Dependencies/FeeConcession/list.html', context) 

# @login_required(login_url='login_url')
def section_list(request):
    sec = Section.objects.all()
    context = {'section': sec}
    return render(request, 'Dependencies/Sections/list.html', context)

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def sections(request):
    if request.method == 'POST':
        user_form = section_form(request.POST)
        if user_form.is_valid():
            sections = user_form.save()
            context = {
                'return': 'Has been added successfully'
            }
            return render(request,'Dependencies/Sections/created_sections_form.html', context)
        else:
            context = {
                'return': 'Is not valid'
            }
            return render(request,'Dependencies/Sections/created_sections_form.html', context)
    else:
        user_form = section_form()
        return render(request,'Dependencies/Sections/sections_form.html',{'user_form':user_form})

def section_upload(request):
    template = "Dependencies/Sections/section_upload.html"

    prompt = {
        'order': 'Order of the CSV should be sect_code, sect_name, remarks'
    }

    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Section.objects.update_or_create(
            sect_code=column[0],
            sect_name=column[1],
            remarks=column[2]          
        )
    print(created)
    context = {'sec': 'Added Successfully'}
    return render(request, template, context)

def section_download(request):

    items = Section.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Section.csv"'

    writer = csv.writer(response, delimiter=',')
    writer.writerow(['section_code', 'section_name', 'remarks'])

    return response

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def edit_section(request, sect_code):
    sec = get_object_or_404(Section, sect_code=sect_code)

    if request.method == "POST":
        user_form = section_form(request.POST or None, instance=sec)
        if user_form.is_valid():
            user_form.save()
            return redirect('section_list')
    else:
        user_form = section_form(instance=sec)

        return render(request, 'Dependencies/Sections/editsection.html', {'user_form': user_form})

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def delete_section(request, sect_code):
    Section.objects.filter(sect_code=sect_code).delete()
    sect = Section.objects.all()

    context = {
        'section' : sect
    }
    return render(request, 'Dependencies/Sections/list.html', context)
            

# @login_required(login_url='login_url')
def session_list(request):
    sess = Session.objects.all()
    context = {'session': sess}
    return render(request, 'Dependencies/Sessions/list.html', context)

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def sessions(request):
    if request.method == 'POST':
        user_form = session_form(request.POST)
        if user_form.is_valid():
            sessions = user_form.save()
            context = {
                'return': 'Has been added successfully'
            }
            return render(request,'Dependencies/Sessions/created_sessions_form.html', context)
        else:
            context = {
                'return': 'Is not valid'
            }
            return render(request,'Dependencies/Sessions/created_sessions_form.html', context)
    else:
        user_form = session_form()
        return render(request,'Dependencies/Sessions/sessions_form.html',{'user_form':user_form})

def session_upload(request):
    template = "Dependencies/Sessions/session_upload.html"

    prompt = {
        'order': 'Order of the CSV should be session_code, session_name'
    }

    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Session.objects.update_or_create(
            session_code=column[0],
            session_name=column[1]         
        )
    print(created)
    context = {'ses': 'Added Successfully'}
    return render(request, template, context)

def session_download(request):

    items = Session.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Session.csv"'

    writer = csv.writer(response, delimiter=',')
    writer.writerow(['session_code', 'session_name'])

    return response

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def edit_session(request, session_code):
    sess = get_object_or_404(Session, session_code=session_code)

    if request.method == "POST":
        user_form = session_form(request.POST or None, instance=sess)
        if user_form.is_valid():
            user_form.save()
            return redirect('session_list')
    else:
        user_form = session_form(instance=sess)

        return render(request, 'Dependencies/Sessions/editsession.html', {'user_form': user_form})

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def delete_session(request, session_code):
    Session.objects.filter(session_code=session_code).delete()
    sessi = Session.objects.all()

    context = {
        'session' : sessi
    }
    return render(request, 'Dependencies/Sessions/list.html', context)

# @login_required(login_url='login_url')  
def religion_list(request):
    reli = Religion.objects.all()
    context = {'religion': reli}
    return render(request, 'Dependencies/Religions/list.html', context)

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def religions(request):
    if request.method == 'POST':
        user_form = religion_form(request.POST)
        if user_form.is_valid():
            religions = user_form.save()
            context = {
                'return': 'Has been added successfully'
            }
            return render(request,'Dependencies/Religions/created_religions_form.html', context)
        else:
            context = {
                'return': 'Is not valid'
            }
            return render(request,'Dependencies/Religions/created_religions_form.html', context)
    else:
        user_form = religion_form()
        return render(request,'Dependencies/Religions/religions_form.html',{'user_form':user_form})

def religion_upload(request):
    template = "Dependencies/Religions/religion_upload.html"

    prompt = {
        'order': 'Order of the CSV should be religion_code, religion'
    }

    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Religion.objects.update_or_create(
            religion_code=column[0],
            religion=column[1]         
        )
    print(created)
    context = {'rel': 'Added Successfully'}
    return render(request, template, context)

def religion_download(request):

    items = Religion.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Religion.csv"'

    writer = csv.writer(response, delimiter=',')
    writer.writerow(['religion_code', 'religion'])

    return response


# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def edit_religion(request, religion_code):
    reli = get_object_or_404(Religion, religion_code=religion_code)

    if request.method == "POST":
        user_form = religion_form(request.POST or None, instance=reli)
        if user_form.is_valid():
            user_form.save()
            return redirect('religion_list')
    else:
        user_form = religion_form(instance=reli)

        return render(request, 'Dependencies/Religions/editreligion.html', {'user_form': user_form})

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def delete_religion(request, religion_code):
    Religion.objects.filter(religion_code=religion_code).delete()
    relig = Religion.objects.all()

    context = {
        'religion' : relig
    }
    return render(request, 'Dependencies/Religions/list.html', context)

# @login_required(login_url='login_url')
def subject_list(request):
    sub = Subject.objects.all()
    context = {'subject': sub}
    return render(request, 'Dependencies/Subjects/list.html', context)

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def subjects(request):
    if request.method == 'POST':
        user_form = subject_form(request.POST)
        if user_form.is_valid():
            subjects = user_form.save()
            context = {
                'return': 'Has been added successfully'
            }
            return render(request,'Dependencies/Subjects/created_subjects_form.html', context)
        else:
            context = {
                'return': 'Is not valid'
            }
            return render(request,'Dependencies/Subjects/created_subjects_form.html', context)
    else:
        user_form = subject_form()
        return render(request,'Dependencies/Subjects/subjects_form.html',{'user_form':user_form})


def subject_upload(request):
    template = "Dependencies/Subjects/subject_upload.html"

    prompt = {
        'order': 'Order of the CSV should be subject_code, subjects'
    }

    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Subject.objects.update_or_create(
            subject_code=column[0],
            subjects=column[1]         
        )
    print(created)
    context = {'sub': 'Added Successfully'}
    return render(request, template, context)

def subject_download(request):

    items = Subject.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Subject.csv"'

    writer = csv.writer(response, delimiter=',')
    writer.writerow(['subject_code', 'subjects'])

    return response

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def edit_subject(request, subject_code):
    sub = get_object_or_404(Class_Subject, subject_code=subject_code)

    if request.method == "POST":
        user_form = subject_form(request.POST or None, instance=sub)
        if user_form.is_valid():
            user_form.save()
            return redirect('subject_list')
    else:
        user_form = subject_form(instance=sub)

        return render(request, 'Dependencies/Subjects/editsubject.html', {'user_form': user_form})

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def delete_subject(request, subject_code):

    Subject.objects.filter(subject_code=subject_code).delete()
    subje = Subject.objects.all()

    context = {
        'subject' : subje
    }
    return render(request, 'Dependencies/Subjects/list.html', context)


def CLASS():
    Cla = Class.objects.all()
    return Cla

def C_SUBJ():
    sub = Class_Subject.objects.all()
    return sub

# @login_required(login_url='login_url')
def class_subject_list(request):
    if request.method == 'POST':
        InClass = request.POST.get('class')
        classes = CLASS()
        lis = get_list_or_404(Class_Subject, Class_id = InClass)
        context = {
            'subjec': lis,
            'class': classes,
        }
        return render(request, 'Dependencies/Class_Subjects/list.html', context)
    else:
        classes = CLASS()
        bas = C_SUBJ()
        context = {
            # 'subjec': bas,
            'class': classes,
        }
        return render(request, 'Dependencies/Class_Subjects/list.html', context)

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def class_subjects(request):
    if request.method == 'POST':
        rawdata = request.POST
        class_ = rawdata.get('Class')
        subject = rawdata.getlist('subject' , default=1)
        class__ = get_object_or_404(Class , class_code = class_ )
        for i in subject:
            subject_ = get_object_or_404(Subject , subject_code = i )
            print(class__)
            print(subject_)
            user_form = classes_subject_form({
                'Class' : class__ ,
                'class_subjects' : subject_ ,
            })
        # user_form = classes_subject_form(request.POST)
            if user_form.is_valid():
                user_form.save()
            
        return redirect('class_subject_form')
        # return render(request,'Dependencies/Class_Subjects/class_subject_form.html' , context)
        # else:
        #     context = {
        #         'return': 'Is not valid'
        #     }
        #     return render(request,'Dependencies/Class_Subjects/created_class_subject_form.html', context)
    else:
        sub = Subject.objects.all()
        user_form = classes_subject_form()
        return render(request,'Dependencies/Class_Subjects/class_subject_form.html',{'user_form':user_form,'subject':sub})

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def edit_class_subject(request, Class_code):
    cla_sub = get_object_or_404(Class_Subject, Class_code=Class_code)

    if request.method == "POST":
        user_form = classes_subject_form(request.POST or None, instance=cla_sub)
        if user_form.is_valid():
            user_form.save()
            return redirect('class_subject_list')
    else:
        user_form = classes_subject_form(instance=cla_sub)

        return render(request, 'Dependencies/Class_Subjects/editclasssubject.html', {'user_form': user_form})

# @login_required(login_url='login_url')
def class_subject_detail(request,Class_code):
    kla = get_object_or_404(Class_Subject,Class_code = Class_code)
    context = {
        'class_subject': kla,
    }
    return render(request, 'Dependencies/Class_Subjects/detail.html', context)

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def delete_class_subject(request, Class_code):
    
    Class_Subject.objects.filter(Class_code=Class_code).delete()
    cla_subj = Class_Subject.objects.all()

    context = {
        'class_subject' : cla_subj
    }
    return render(request, 'Dependencies/Class_Subjects/list.html', context)

# @login_required(login_url='login_url')
def fee_type_list(request):
    feT = Fee_Type.objects.all()
    context = {'fee_type': feT}
    return render(request, 'Dependencies/FeeType/list.html', context)

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def fee_type(request):
    if request.method == 'POST':
        user_form = fee_type_form(request.POST)
        if user_form.is_valid():
            fee_type = user_form.save()
            context = {
                'return': 'Has been added successfully'
            }
            return render(request,'Dependencies/FeeType/created_fee_type_form.html', context)
        else:
            context = {
                'return': 'Is not valid'
            }
            return render(request,'Dependencies/FeeType/created_fee_type_form.html', context)
    else:
        user_form = fee_type_form()
        return render(request,'Dependencies/FeeType/fee_type_form.html',{'user_form':user_form})


def fee_type_upload(request):
    template = "Dependencies/FeeType/fee_type_upload.html"

    prompt = {
        'order': 'Order of the CSV should be fee_type_code, fee_type, description'
    }

    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Fee_Type.objects.update_or_create(
            fee_type_code=column[0],
            fee_type=column[1],
            description=column[2]         
        )
    print(created)
    context = {'pri': 'Added Successfully'}
    return render(request, template, context)

def fee_type_download(request):

    items = Fee_Type.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Fee_Type.csv"'

    writer = csv.writer(response, delimiter=',')
    writer.writerow(['fee_type_code', 'fee_type', 'description'])

    return response

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def edit_fee_type(request, fee_type_code):
    feT = get_object_or_404(Fee_Type, fee_type_code=fee_type_code)

    if request.method == "POST":
        user_form = fee_type_form(request.POST or None, instance=feT)
        if user_form.is_valid():
            user_form.save()
            return redirect('fee_type_list')
    else:
        user_form = fee_type_form(instance=feT)

        return render(request, 'Dependencies/FeeType/editfeetype.html', {'user_form': user_form})

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def delete_fee_type(request, fee_type_code):
    
    Fee_Type.objects.filter(fee_type_code=fee_type_code).delete()
    fT = Fee_Type.objects.all()

    context = {
        'fee_type' : fT
    }
    return render(request, 'Dependencies/FeeType/list.html', context)


# @login_required(login_url='login_url')
# def month_list(request):
#     mon = Month.objects.all()
#     context = {'month': mon}
#     return render(request, 'Dependencies/Months/list.html', context)

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
# def months(request):
#     if request.method == 'POST':
#         user_form = month_form(request.POST)
#         if user_form.is_valid():
#             months = user_form.save()
#             context = {
#                 'return': 'Has been added successfully'
#             }
#             return render(request,'Dependencies/Months/created_month_form.html', context)
#         else:
#             context = {
#                 'return': 'Is not valid'
#             }
#             return render(request,'Dependencies/Months/created_month_form.html', context)
#     else:
#         user_form = month_form()
#         return render(request,'Dependencies/Months/month_form.html',{'user_form':user_form})

# # @login_required(login_url='login_url')
def city_list(request):
    cit = City.objects.all()
    context = {'city': cit}
    return render(request, 'Dependencies/Cities/list.html', context)

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def cities(request):
    if request.method == 'POST':
        user_form = city_form(request.POST)
        if user_form.is_valid():
            cities = user_form.save()
            context = {
                'return': 'Has been added successfully'
            }
            return render(request,'Dependencies/Cities/created_city_form.html', context)
        else:
            context = {
                'return': 'Is not valid'
            }
            return render(request,'Dependencies/Cities/created_city_form.html', context)
    else:
        user_form = city_form()
        return render(request,'Dependencies/Cities/city_form.html',{'user_form':user_form})


def city_upload(request):
    template = "Dependencies/Cities/city_upload.html"

    prompt = {
        'order': 'Order of the CSV should be city_code, cities'
    }

    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = City.objects.update_or_create(
            city_code=column[0],
            cities=column[1]        
        )
    print(created)
    context = {'cit': 'Added Successfully'}
    return render(request, template, context)

def city_download(request):

    items = City.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="City.csv"'

    writer = csv.writer(response, delimiter=',')
    writer.writerow(['city_code', 'cities'])

    return response



