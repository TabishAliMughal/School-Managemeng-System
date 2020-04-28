from django.shortcuts import render , get_list_or_404 , get_object_or_404 , HttpResponse
from .models import *
from student_information.models import *
from dependencies.models import *
import datetime
from .forms import *
from static.renderer import PdfMaker


def CLA():
    Cla = Class.objects.all()
    return Cla

def SEC():
    Sec = Section.objects.all()
    return Sec

def GR():
    gr = Gr.objects.all()
    return gr

def attendance_ask_print(request):
    classes = CLA()
    section = SEC()
    tdate = datetime.date.today()
    log = {
        'class' : classes,
        'section' : section,
        }
    return render(request, 'attendence_ask_print.html', log)

def attendance_print(request):
    if request.method == 'POST':
        rawdata = request.POST
        InClass = rawdata.get('class')
        OutClass = get_object_or_404(Class , class_code = InClass )
        InSection = rawdata.get('section')
        OutSection = get_object_or_404(Section , sect_code = InSection )
        InDate = rawdata.get('date')
        lis = get_list_or_404(SaveAttendence , classes = InClass , sections = InSection , date = InDate)
        context = {
            'InClass' : OutClass ,
            'InSection' : OutSection ,
            'InDate' : InDate ,
            'abc' : lis ,
        }
        pdf = PdfMaker('attendence_print.html', context)
        return HttpResponse(pdf, content_type='application/pdf')

def attendance_save(CreateView):
    if CreateView.method == "POST":
        rawdata = CreateView.POST
        InGr = rawdata.getlist('gr' , default='1')
        InName = rawdata.getlist('name' , default='1')
        InClass = rawdata.getlist('class' , default='1')
        InSection = rawdata.getlist('section' , default='1')
        InDate = rawdata.getlist('date' , default='1')
        count = '0'
        for i in InGr:
            count = int(count)+1
            In_f_Gr = get_object_or_404(Gr ,gr_number = InGr[count - 1])
            InAttended = rawdata.get(str(In_f_Gr.gr_number))
            In_f_Family = get_object_or_404(Family ,surname = In_f_Gr.family_code)
            In_f_Class = get_object_or_404(Class ,class_name = InClass[count - 1])
            In_f_Section = get_object_or_404(Section ,sect_name = InSection[count - 1])
            InAttended = rawdata.get(str(In_f_Gr.gr_number))
            form = Attendence_Form({
                'gr' : (In_f_Gr.gr_number) ,
                'family' : (In_f_Family.family_code) ,
                'classes' : (In_f_Class.class_code) ,
                'sections' : (In_f_Section.sect_code) ,
                'attendence' : (InAttended) ,
                'date' : (InDate[count - 1]) ,
            })
            if form.is_valid:
                form.save()
    return render(CreateView, 'attendence_saved.html')

def attendance_add(CreateView):
    if CreateView.method == 'POST':
        InClasses = CreateView.POST.get('class')
        InSection = CreateView.POST.get('section')
        InDate = CreateView.POST.get('date')
        classes = CLA()
        section = SEC()
        tdate = datetime.date.today()
        if InClasses == '' and InSection == '':
            lis = Gr.objects.all()
        elif InSection == '':
            lis = get_list_or_404(Gr , current_class = InClasses)
        elif InClasses == '':
            lis = get_list_or_404(Gr , section = InSection)
        else:
            lis = get_list_or_404(Gr , section = InSection , current_class = InClasses)
        log = {
            'attend' : lis,
            'class' : classes,
            'section' : section,
            'date' : InDate,
            'tdate' : tdate,
            }
        return render(CreateView, 'attendence_for_all.html',log)
    else:
        classes = CLA()
        section = SEC()
        clas = GR()
        date = ''
        tdate = datetime.date.today()
        log = {
            'attend' : clas,
            'class' : classes,
            'section' : section,
            'date' : date,
            'tdate' : tdate,
            }
        return render(CreateView, 'attendence_for_all.html', log)