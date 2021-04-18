from django.shortcuts import render, redirect
from UserAuthentication.views import login_required
from UserAuthentication.models import User, Doctor
from .models import Appointment
from datetime import datetime

@login_required
def index_appointments(request):
    # print(request.session['user_id'])
    # print(User.objects.get(id=request.session['user_id']))
    # print(Appointment.objects.filter(user=request.session['user_id']))
    # print(Appointment.objects.filter(user=1))

    no_appointments = True
    if Appointment.objects.filter(user=request.session['user_id']):
        no_appointments = False

    # print(request.session['user_id'], no_appointments)
    appointments = list(filter(lambda appointment: appointment.from_date_time.replace(tzinfo=utc) < datetime.now().replace(tzinfo=utc), Appointment.objects.filter(user=request.session['user_id'])))
    print(Appointment.objects.filter(user=request.session['user_id']))
    print(datetime.now())
    print("Appointments: ", appointments)

    appo = Appointment.objects.filter(user=request.session['user_id'])
    aplist = []

    for i in appo:
        
        if i.from_date_time.replace(tzinfo=None) >= datetime.now():
            aplist.append(i)
    

    def skey(a):
        return a.from_date_time

    aplist.sort(key = skey)
    context = {
        'no_appointments': no_appointments,
        'appointments': aplist,
        'user': User.objects.get(id=request.session['user_id'])
    }

    return render(request, 'appointments.html', context)


def index_book_appointment(request):
    # print('Book appointment')
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'book_appointment.html', context)

def index_appointment_info(request):
    if request.method == "POST":
        title = request.POST['Appointment_Title']
        description = request.POST['description']
        date_time = request.POST['time']

        # print(title, description, date_time)

        # print(request.session.keys())

        request.session['appointment_title'] = title
        request.session['appointment_description'] = description
        request.session['appointment_data_time'] = date_time

        # print(request.session.keys())

    return redirect('/recommendations')

def index_cancel_appointment(request, id):
    print(id)
    print(Appointment.objects.get(id=id))
    Appointment.objects.get(id=id).delete()
    return redirect('/appointments')
