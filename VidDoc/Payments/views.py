from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as auth_login
from django.conf import settings
from .models import Transaction
from .paytm import generate_checksum, verify_checksum
from datetime import datetime, timedelta

from django.views.decorators.csrf import csrf_exempt

from Appointments.models import Appointment
from UserAuthentication.models import User,Doctor

def payment(request):
    context={}
    
    try:
        print(request.session.keys())
        # print(request.session['doctor_id'])
        print(request.session['appointment_data_time'])
        from_date_time = datetime.strptime(request.session['appointment_data_time'], '%m/%d/%Y %I:%M %p')
        print(from_date_time)
        to_date_time = from_date_time + timedelta(hours =1)
        print(to_date_time)
        # print(Doctor.objects.get(id = request.session['doctor_id']).amount)
        amount = Doctor.objects.get(id = request.session['doctor_id']).amount
        context['amount'] = amount
        try:
            phno = request.POST['phno']
            context['phno'] = phno
            if phno == '7777777777':
                try:
                    otp = request.POST['otp']
                    context['otp'] = otp
                    if otp == '489871':
                        context['status']='Doctor Succesfully Appointed'
                        context['success']='button'
                        if not Appointment.objects.filter(user = User.objects.get(id = request.session['user_id']), doctor = Doctor.objects.get(id = request.session['doctor_id']),link ='https://meet.google.com/vsw-iswr-axj', title = request.session['appointment_title'], description =request.session['appointment_description'], from_date_time = from_date_time, to_date_time = to_date_time):
                            Appointment(user = User.objects.get(id = request.session['user_id']), doctor = Doctor.objects.get(id = request.session['doctor_id']),link ='https://meet.google.com/vsw-iswr-axj', title = request.session['appointment_title'], description =request.session['appointment_description'], from_date_time = from_date_time, to_date_time = to_date_time).save()

                        del request.session['doctor_id']
                        del request.session['appointment_title']
                        del request.session['appointment_description']
                        del request.session['appointment_data_time']

                        # print(request.session.keys())
                        return render(request, 'payment.html', context=context)
                    else:
                        context['status']='Wrong OTP'
                        return render(request, 'payment.html', context = context)
                except:
                    context['otp'] = True
                    context['status']="enter otp"
                    return render(request, 'payment.html', context = context)
            else:
                context['status']='Wrong Phone number'
                return render(request, 'payment.html', context = context)
        except:
            context['status']='Enter Phone number'
            return render(request, 'payment.html', context = context)
    except:
        print('sup man')
        print(request.session['user_id'])
        return render(request, 'payment.html')
        
        