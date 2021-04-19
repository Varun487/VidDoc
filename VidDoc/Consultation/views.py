from django.shortcuts import render,redirect
from UserAuthentication.views import login_required
from UserAuthentication.models import User, Doctor
from Appointments.models import Appointment
import random
from .models import Prescription
from datetime import datetime

@login_required
def index_consultation(request):
    # print(request.session['user_id'])
    # print(User.objects.get(id=request.session['user_id']))
    # print(Appointment.objects.filter(user=request.session['user_id']))
    # print(Appointment.objects.filter(user=1))

    no_appointments = True
    # print(request.session['user_id'], no_appointments)

    appo = Appointment.objects.filter(user=request.session['user_id'])
    conlist = []

    for i in appo:
        i.from_date_time.replace(tzinfo=None)
        if i.from_date_time.replace(tzinfo=None) < datetime.now():
            conlist.append(i)
    # print(aplist)

    def skey(a):
        return a.from_date_time

    conlist.sort(key = skey, reverse = True)

    no_consultation = True
    if len(conlist)!=0:
        no_consultation = False

    aplist = []

    for i in appo:
        
        if i.from_date_time.replace(tzinfo=None) >= datetime.now():
            aplist.append(i)
    

    aplist.sort(key = skey)

    if len(aplist)!=0:
        no_appointments=False
    context = {
        'no_appointments': no_appointments,
        'no_consultation': no_consultation,
        'appointments': aplist,
        'consultations': conlist,
        'user': User.objects.get(id=request.session['user_id'])
    }

    return render(request, 'consultation.html', context)

def show_prescription(request, id):

    p = []
    p.append({'Name': 'Vicodin, Norco, Xodol (hydrocodone, acetaminophen)', 'drugclass': 'Opioid/acetaminophen combinations', 'Price':'Rs. 300'})
    p.append({'Name':'Synthroid, Levoxyl, Unithroid (levothyroxine)','drugclass':'Thyroxines','Price':'Rs. 200'})
    p.append({'Name':'Delasone, Sterapred (prednisone)','drugclass':'Corticosteroids','Price':'Rs. 100'})
    p.append({'Name':'Amoxil (amoxicillin)','drugclass':'Penicillin antibiotics','Price':'Rs. 100'})
    p.append({'Name':'Neurontin (gabapentin)','drugclass':'Anti-epileptics','Price':'Rs. 120'})
    p.append({'Name':'Prinivil, Zestril (lisinopril)','drugclass':'Angiotensin converting enzyme Inhibitors','Price':'Rs. 70'})
    p.append({'Name':'Lipitor (atorvastatin)','drugclass':'Statin','Price':'Rs. 100'})
    p.append({'Name':'Glucophage (metformin)','drugclass':'Biguanides','Price':'Rs. 90'})
    p.append({'Name':'Zofran (ondansetron)','drugclass':'Serotonin antagonists','Price':'Rs. 110'})
    p.append({'Name':'Motrin (ibuprofen)','drugclass':'Nonsteroidal anti-inflammatory drugs','Price':'Rs. 120'})

    random.shuffle(p)

    consultobj = Appointment.objects.get(id = id)
    context = {}
    context['consultation'] = consultobj
    # context['prescription'] = p[:2]
    try:
        pobj = Prescription.objects.get(appointment = consultobj)
        # print(pobj.prescription)
        # print(type(eval(pobj.prescription)))
        context['prescription'] = eval(pobj.prescription)
    except:
        Prescription(appointment = consultobj, prescription = str(p[:2])).save()
        # print(p[:2])
        context['prescription'] = p[:2]

    return render(request,'prescription.html',context = context)

