from django.shortcuts import render, redirect
from UserAuthentication.models import Doctor

def index_recommendations(request):
    # print(Doctor.objects.all())
    context = {
        'doctors': Doctor.objects.all(),
    }

    return render(request, 'recommendations.html', context)

def index_select_doctor(request):
    # print(Doctor.objects.all())
    if request.method == "POST":
        doctor_id = request.POST['doctor']
        request.session['doctor_id'] = doctor_id
        print(request.session['doctor_id'])

    return redirect('/payments')
