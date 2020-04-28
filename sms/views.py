from django.shortcuts import render , HttpResponse
from dependencies.models import *
from Query.models import *
from student_information.models import *
from .forms import *
import serial
from curses import ascii
from time import sleep
from django.contrib import messages


def ManageSmsView(SmsView):
    if SmsView.method == 'POST':
        Tool = SmsView.POST.get('tool')
        Clas = SmsView.POST.get('clas')
        Sms = SmsView.POST.get('sms')
        Com = SmsView.POST.get('com')
        context = {
            'sms' : Sms,
            'tool' : Tool,
            'clas' : Clas,
        }
        if Tool == 'Sms':
            for gr in Gr.objects.all():
                gr_rows = gr
                for qu in Entry_data.objects.all():
                    qu_rows = qu
                    if str(gr_rows.current_class) == str(Clas):
                        if str(gr_rows.query_code) == str(qu_rows.Name):
                            ph = int(qu_rows.Contact)
                            ser = serial.Serial()
                            ser.port = 'COM'+str(Com)
                            ser.baudrate = 115200
                            ser.timeout = 1
                            ser.open()
                            abc = 'AT+CMGF=1\r\n'
                            ser.write(abc.encode())
                            xyz = 'AT+CPMS="ME","SM","ME"\r\n'
                            ser.write(xyz.encode())
                            def sendsms(number,text):
                                print(number)
                                first = 'AT+CMGF=1\r\n'
                                ser.write(first.encode())
                                sleep(2)
                                second = 'AT+CMGS="%s"\r\n' % number
                                ser.write(second.encode())
                                sleep(2)
                                third = '%s' % text
                                ser.write(third.encode())
                                sleep(2)
                                fourth = ascii.ctrl('z')
                                ser.write(fourth.encode())
                            sendsms(ph,Sms)
        return render(SmsView , 'Sms/Create/created.html',context)

        if Tool == 'WhatsApp':
            pass
    else:
        data = Class.objects.all()
        context = {
            'data' : data
        }
        return render(SmsView , 'Sms/Create/create.html' , context)
