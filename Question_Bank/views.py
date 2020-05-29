import csv, io
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse ,get_object_or_404, get_list_or_404
from .models import Book, Publisher, Chapter, Question_Type, Question_Bank
from .forms import book_form, publisher_form, chapter_form, question_type_form, question_bank_form
from django.contrib.auth.decorators import login_required
from authentication.user_handeling import unauthenticated_user, allowed_users, admin_only
from .filters import Question_Bank_filter
import random 
from dependencies.models import *
from static.renderer import PdfMaker


# Create your views here.

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def book_list(request):
    boo = Book.objects.all()
    clas = Class.objects.all()
    sub = Subject.objects.all()
    publ = Publisher.objects.all()
    context = {'book': boo, 'class': clas, 'subject': sub, 'publisher': publ }
    return render(request, 'Question_Bank/Books/list.html', context)


# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def books(request):
    if request.method == 'POST':
        user_form = book_form(request.POST)
        if user_form.is_valid():
            books = user_form.save()
            context = {
                'return': 'Has been added successfully'
            }
            return render(request,'Question_Bank/Books/created_book_form.html', context)
            
        else:
            context = {
                'return': 'Is not valid'
            }
            return render(request,'Question_Bank/Books/created_book_form.html', context)
    else:
        user_form = book_form()
        return render(request,'Question_Bank/Books/book_form.html',{'user_form':user_form})

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def book_upload(request):
    template = "Question_Bank/Books/book_upload.html"

    prompt = {
        'order': 'Order of the CSV should be book_code, book_name, classes, subject, publisher, medium'
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
        # _, created = Book.objects.update_or_create(
        created = book_form({
            'book_code' : column[0],
            'book_name' : column[1],
            'classes' : column[2],
            'subject' : column[3],
            'publisher' : column[4],
            'medium' : column[5],
        })
        created.save()
    context = {}
    return render(request, template, context)

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def book_download(request):
    items = Book.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="books.csv"'
    writer = csv.writer(response, delimiter=',')
    writer.writerow(['book_code', 'book_name', 'classes', 'subject', 'publisher', 'medium'])
    return response

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def edit_book(request,book_code):
    boo = get_object_or_404(Book, book_code=book_code)
    if request.method == "POST":
        user_form = book_form(request.POST or None, instance=boo)
        if user_form.is_valid():
            user_form.save()
            context = {
                'return': 'Has been added successfully'
            }
            return render(request,'Question_Bank/Books/created_book_form.html', context)
    else:
        user_form = book_form(instance=boo)

        return render(request, 'Question_Bank/Books/editbook.html', {'user_form': user_form})

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def book_detail(request,book_code):
    bk = get_object_or_404(Book,book_code = book_code)
    context = {
        'book': bk,
    }
    return render(request, 'Question_Bank/Books/detail.html', context)

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def delete_book(request, book_code):
    Book.objects.filter(book_code=book_code).delete()
    bo = Book.objects.all()
    context = {
        'book' : bo
    }
    return render(request, 'Question_Bank/Books/list.html', context) 

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def ManageBookPrintPdfView(PrintView,clas,subj,publ):
    if PrintView.method == 'POST':
        Class_ = get_object_or_404(Class , class_name = clas)
        Sub = get_object_or_404(Subject , subjects = subj)
        publi = get_object_or_404(Publisher , publisher_name = publ)
        lis = get_list_or_404(Book , classes = Class_.class_code , subject = Sub.subject_code, publisher = publi.publisher_code)
        context = {
            'abc' : lis ,
            'one' : clas ,
            'two' : subj ,
            'three' : publ ,
        }
        pdf = PdfMaker('Question_Bank/Books/print.html', context)
        return HttpResponse(pdf, content_type='application/pdf')

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def publisher_list(request):
    pub = Publisher.objects.all()
    context = {'publisher': pub}
    return render(request, 'Question_Bank/Publishers/list.html', context)

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def publishers(request):
    if request.method == 'POST':
        user_form = publisher_form(request.POST)
        if user_form.is_valid():
            publishers = user_form.save()
            context = {
                'return': 'Has been added successfully'
            }
            return render(request,'Question_Bank/Publishers/created_publisher_form.html', context)
        else:
            context = {
                'return': 'Is not valid'
            }
            return render(request,'Question_Bank/Publishers/created_publisher_form.html', context)
    else:
        user_form = publisher_form()
        return render(request,'Question_Bank/Publishers/publisher_form.html',{'user_form':user_form})

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def publisher_upload(request):
    template = "Question_Bank/Publishers/publisher_upload.html"

    prompt = {
        'order': 'Order of the CSV should be publisher_code, publisher_name, city'
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
        # _, created = Book.objects.update_or_create(
        created = publisher_form({
            'publisher_code' : column[0],
            'publisher_name' : column[1],
            'city' : column[2],
        })
        created.save()
    context = {}
    return render(request, template, context)

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def publisher_download(request):
    items = Publisher.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="publishers.csv"'
    writer = csv.writer(response, delimiter=',')
    writer.writerow(['publisher_code', 'publisher_name', 'city'])
    return response

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def edit_publisher(request,publisher_code):
    pub = get_object_or_404(Book, publisher_code=publisher_code)
    if request.method == "POST":
        user_form = publisher_form(request.POST or None, instance=pub)
        if user_form.is_valid():
            user_form.save()
            context = {
                'return': 'Has been added successfully'
            }
            return render(request,'Question_Bank/Publishers/created_publisher_form.html', context)
    else:
        user_form = publisher_form(instance=pub)

        return render(request, 'Question_Bank/Publishers/editpublisher.html', {'user_form': user_form})

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def delete_publisher(request, publisher_code):
    Publisher.objects.filter(publisher_code=publisher_code).delete()
    publi = Publisher.objects.all()

    context = {
        'publisher' : publi
    }
    return render(request, 'Question_Bank/Publishers/list.html', context)

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def ManagePublisherPrintPdfView(PrintView):
    publi = Publisher.objects.all()
    context = {
        'abc' : publi ,
    }
    pdf = PdfMaker('Question_Bank/Publishers/print.html', context)
    return HttpResponse(pdf, content_type='application/pdf') 

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def chapter_list(request):
    chap = Chapter.objects.all()
    context = {'chapter': chap}
    return render(request, 'Question_Bank/Chapters/list.html', context)

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def chapters(request):
    if request.method == 'POST':
        user_form = chapter_form(request.POST)
        if user_form.is_valid():
            chapters = user_form.save()
            context = {
                'return': 'Has been added successfully'
            }
            return render(request,'Question_Bank/Chapters/created_chapter_form.html', context)
        else:
            context = {
                'return': 'Is not valid'
            }
            return render(request,'Question_Bank/Chapters/created_chapter_form.html', context)
    else:
        user_form = chapter_form()
        return render(request,'Question_Bank/Chapters/chapter_form.html',{'user_form':user_form})

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def chapter_upload(request):
    template = "Question_Bank/Chapters/chapter_upload.html"
    prompt = {
        'order': 'Order of the CSV should be chapter_code, chapter_name, books'
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
        # _, created = Book.objects.update_or_create(
        created = chapter_form({
            'chapter_code' : column[0],
            'chapter_name' : column[1],
            'books' : column[2],
        })
        created.save()
    context = {}
    return render(request, template, context)

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def chapter_download(request):
    items = Chapter.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="chapters.csv"'
    writer = csv.writer(response, delimiter=',')
    writer.writerow(['chapter_code', 'chapter_name', 'books'])
    return response

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def edit_chapter(request,chapter_code):
    chap = get_object_or_404(Chapter, chapter_code=chapter_code)
    if request.method == "POST":
        user_form = chapter_form(request.POST or None, instance=chap)
        if user_form.is_valid():
            user_form.save()
            context = {
                'return': 'Has been added successfully'
            }
            return render(request,'Question_Bank/Chapters/created_chapter_form.html', context)
    else:
        user_form = chapter_form(instance=chap)
        return render(request, 'Question_Bank/Chapters/editchapter.html', {'user_form': user_form})

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def delete_chapter(request, chapter_code):
    Chapter.objects.filter(chapter_code=chapter_code).delete()
    chapt = Chapter.objects.all()
    context = {
        'chapter' : chapt
    }
    return render(request, 'Question_Bank/Chapters/list.html', context)

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def ManageChapterPrintPdfView(PrintView):
    chp = Chapter.objects.all()
    context = {
        'abc' : chp ,
    }
    pdf = PdfMaker('Question_Bank/Chapters/print.html', context)
    return HttpResponse(pdf, content_type='application/pdf')

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def question_type_list(request):
    QT = Question_Type.objects.all()
    context = {'question_type': QT}
    return render(request, 'Question_Bank/Question_Type/list.html', context)

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def questions_types(request):
    if request.method == 'POST':
        user_form = question_type_form(request.POST)
        if user_form.is_valid():
            question_types = user_form.save()
            context = {
                'return': 'Has been added successfully'
            }
            return render(request,'Question_Bank/Question_Type/created_question_type_form.html', context)
            
        else:
            context = {
                'return': 'Is not valid'
            }
            return render(request,'Question_Bank/Question_Type/created_question_type_form.html', context)
    else:
        user_form = question_type_form()
        return render(request,'Question_Bank/Question_Type/question_type_form.html',{'user_form':user_form})

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def question_type_upload(request):
    template = "Question_Bank/Question_Type/question_type_upload.html"
    prompt = {
        'order': 'Order of the CSV should be Q_type_code, question_type'
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
        # _, created = Book.objects.update_or_create(
        created = question_type_form({
            'Q_type_code' : column[0],
            'question_type' : column[1],
        })
        created.save()
    context = {}
    return render(request, template, context)

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def Q_type_download(request):
    items = Question_Type.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Question_type.csv"'

    writer = csv.writer(response, delimiter=',')
    writer.writerow(['Q_type_code', 'question_type'])

    return response

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def edit_question_type(request,Q_type_code):
    QT = get_object_or_404(Question_Type, Q_type_code=Q_type_code)
    if request.method == "POST":
        user_form = question_type_form(request.POST or None, instance=QT)
        if user_form.is_valid():
            user_form.save()
            context = {
                'return': 'Has been added successfully'
            }
            return render(request,'Question_Bank/Question_Type/created_question_type_form.html', context)
    else:
        user_form = question_type_form(instance=QT)
        return render(request, 'Question_Bank/Question_Type/editquestiontype.html', {'user_form': user_form})

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def delete_question_type(request, Q_type_code):
    Question_Type.objects.filter(Q_type_code=Q_type_code).delete()
    quesT = Question_Type.objects.all()
    context = {
        'question_type' : quesT
    }
    return render(request, 'Question_Bank/Question_Type/list.html', context)


# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def filtered_Questions(request):
    if request.method == 'POST':
        a = (request.POST.getlist('abc'))
        b = (request.POST.getlist('type'))
        v = '0'
        c = []
        for i in a:
            c.append([a[int(v)],b[int(v)]])
            v = int(v) + 1
        InSubject = request.POST.get('subject')
        InClass = request.POST.get('classes')
        InBook = request.POST.get('book')
        InChapter = request.POST.get('chapter')
        InQuantity = request.POST.get('qty')
        # quest_type = Question_Type.objects.all()
        context = {'question_bank': 'No Matching Questions Found'}
        all = Question_Bank.objects.all()
        ben = []
        for i in all:
            ben.append(i)
        random.shuffle(ben)
        Ques = []
        # for i in range(0,int(InQuantity)):
        endques = []
        for s in range(0,int(InQuantity)):
            for t in c:
                qtype = [t[0]]
                for i in ben:
                    if str(i.subject.pk) == str(InSubject) and str(i.classes.pk) == str(InClass) and str(i.book.pk) == str(InBook) and str(i.chapter.pk) == str(InChapter) and str(i.question_type) == str(t[0]):
                        qtype.append(i.question)
                finalques = []
                for v in Ques:
                    abc = []
                    for i in c:
                        if str(i[0]) == str(v[0]):
                            f = (v[1:int(i[1])+1])
                            for k in f:
                                abc.append(k)
                        random.shuffle(abc)
                        finalques.append({'type':v[0],'ques':abc})
            endques.append(finalques)
        # print(finalques)
        context = {'finalques':endques}
        # return render(request,'Question_Bank/Question_Bank/print.html',context)
        pdf = PdfMaker('Question_Bank/Question_Bank/print.html', context)
        return HttpResponse(pdf, content_type='application/pdf')


# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def question_banks(request):
    if request.method == 'POST':
        user_form = question_bank_form(request.POST)
        if user_form.is_valid():
            question_banks = user_form.save()
            context = {
                'return': 'Has been added successfully'
            }
            return render(request,'Question_Bank/Question_Bank/created_question_bank_form.html', context)
        else:
            context = {
                'return': 'Is not valid'
            }
            return render(request,'Question_Bank/Question_Bank/created_question_bank_form.html', context)
    else:
        user_form = question_bank_form()
        return render(request,'Question_Bank/Question_Bank/question_bank_form.html',{'user_form':user_form})

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def question_bank_upload(request):
    template = "Question_Bank/Question_Bank/question_bank_upload.html"
    prompt = {
        'order': 'Order of the CSV should be question_code, question, subject, classes, publisher, chapter, question_type, question_from'
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
        # _, created = Book.objects.update_or_create(
        created = question_bank_form({
            'question_code' : column[0],
            'question' : column[1],
            'subject' : column[2],
            'classes' : column[3],
            'publisher' : column[4],
            'chapter' : column[5],
            'question_type' :column[6],
            'question_from' : column[7]
        })
        created.save()
    context = {}
    return render(request, template, context)

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def Q_bank_download(request):
    items = Question_Bank.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Question_bank.csv"'
    writer = csv.writer(response, delimiter=',')
    writer.writerow(['question_code', 'question','subject', 'classes', 'publisher', 'chapter', 'question_type', 'question_from'])
    return response

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def edit_question_bank(request,question_code):
    quest = get_object_or_404(Question_Bank, question_code=question_code)
    if request.method == "POST":
        user_form = question_bank_form(request.POST or None, instance=quest)
        if user_form.is_valid():
            user_form.save()
            context = {
                'return': 'Has been added successfully'
            }
            return render(request,'Question_Bank/Question_Bank/created_question_bank_form.html', context)
    else:
        user_form = question_bank_form(instance=quest)
        return render(request, 'Question_Bank/Question_Bank/editquestionbank.html', {'user_form': user_form})

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def question_bank_detail(request,question_code):
    queb = get_object_or_404(Question_Bank,question_code = question_code)
    context = {
        'question_bank': queb,
    }
    return render(request, 'Question_Bank/Question_Bank/detail.html', context)

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def delete_question_bank(request, question_code):
    Question_Bank.objects.filter(question_code=question_code).delete()
    QB = Question_Bank.objects.all()

    context = {
        'question_bank' : QB
    }
    return render(request, 'Question_Bank/Question_Bank/list.html', context) 

# @login_required(login_url='login_url')
# @allowed_users(allowed_roles=['Admin','Accountant'])
def ManageQuestionPrintPdfView(PrintView):
    Quest = Question_Bank.objects.all()
    context = {
        'abc' : Quest ,
    }
    pdf = PdfMaker('Question_Bank/Question_Bank/print.html', context)
    return HttpResponse(pdf, content_type='application/pdf')


def CLASS():
    Cla = Class.objects.all()
    return Cla


def SUBJ():
    Sub = Subject.objects.all()
    return Sub


def PUBLI():
    pub = Publisher.objects.all()
    return pub

def BOOK():
    bo = Book.objects.all()
    return bo

def CHAP():
    cha = Chapter.objects.all()
    return cha

def QTYPE():
    q_type = Question_Type.objects.all()
    return q_type

def Q_BANK():
    q_bank = Question_Bank.objects.all()
    return q_bank

def book_list(request):
    if request.method == 'POST':
        InClass = request.POST.get('class')
        InSubject = request.POST.get('subject')
        InPublisher = request.POST.get('publisher')
        classes = CLASS()
        subjects = SUBJ()
        publishers = PUBLI()
        if InClass == '' and InSubject == '':
            lis = Book.objects.all()
        elif InSubject == '':
            lis = get_list_or_404(Book, classes = InClass)
        elif InClass == '':
            lis = get_list_or_404(Book, subject = InSubject)
        elif InPublisher == '':
            lis = get_list_or_404(Book, publisher = InPublisher)
        else:
            lis = get_list_or_404(Book, classes = InClass, subject = InSubject, publisher = InPublisher)
        data = {
            'book': lis,
            'class': classes,
            'subject': subjects,
            'publisher': publishers,
        }
        return render(request, 'Question_Bank/Books/list.html', data)
    else:
        classes = CLASS()
        subjects = SUBJ()
        publishers = PUBLI()
        boo = BOOK()
        data = {
            'book' : boo,
            'class': classes,
            'subject': subjects,
            'publisher': publishers,
            }
        return render(request, 'Question_Bank/Books/list.html', data)


def question_bank_list(request):
    lists = Question_Bank.objects.all()
    myFilter = question_bank_form()
    # context = {'question_bank': lists , 'myFilter' : myFilter}
    # return render(request, 'Question_Bank/Question_Bank/list.html', context)
    if request.method == 'POST':
        lists = Question_Bank.objects.all()
        myFilter = question_bank_form()
        context = {'question_bank': lists , 'myFilter' : myFilter}
        InClasses = request.POST.get('class_')
        InSubjects = request.POST.get('subject_')
        InBook = request.POST.get('book_')
        InChapter = request.POST.get('chapter_')
        InQType = request.POST.get('quest_type_')
        classes_ = CLASS()
        subjects_ = SUBJ()
        books_ = BOOK()
        chapters_ = CHAP()
        quest_types_ = QTYPE()
        if InClasses == '' and InSubjects == '' and InBook == '' and InChapter == '' and InQType == '':
            lists = Question_Bank.objects.all()
        elif InSubjects == '':
            lists = get_list_or_404(Question_Bank, classes = InClasses)
        elif InClasses == '':
            lists = get_list_or_404(Question_Bank, subject = InSubjects)
        elif InBook == '':
            lists = get_list_or_404(Question_Bank, book = InBook)
        elif InChapter == '':
            lists = get_list_or_404(Question_Bank, chapter = InChapter)
        elif InQType == "":
            lists = get_list_or_404(Question_Bank, question_type = InQType)
        else:
            lists = get_list_or_404(Question_Bank, classes = InClasses, subject = InSubjects, book = InBook, chapter = InChapter, question_type = InQType)
        code = {
            'q_bank': lists,
            'class' : classes_,
            'subject': subjects_,
            'book' : books_,
            'chapter': chapters_,
            'quest_type': quest_types_,
            'question_bank': lists , 
            'myFilter' : myFilter,
        }
        return render(request, 'Question_Bank/Question_Bank/list.html', code)
    else:
        lists = Question_Bank.objects.all()
        classes_ = CLASS()
        subjects_ = SUBJ()
        books_ = BOOK()
        chapters_ = CHAP()
        quest_types_ = QTYPE()
        quest_bank_ = Q_BANK()
        code = {
            'q_bank' : quest_bank_,
            'class' : classes_,
            'subject': subjects_,
            'book' : books_,
            'chapter': chapters_,
            'quest_type': quest_types_,
            'question_bank': lists , 
            'myFilter' : myFilter,
        }
        return render(request, 'Question_Bank/Question_Bank/list.html')
