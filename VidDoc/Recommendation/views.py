from django.shortcuts import render, redirect
from UserAuthentication.models import User, Doctor
from json import dumps
from django.core import serializers


def index_recommendations(request):
    # print(Doctor.objects.all())
    # print(serializers.serialize('json', Doctor.objects.all()))
    # print(Doctor.objects.all())

    # print(request.session['speciality'])
    # print(request.session['symptoms'])

    specialities = set()
    selected_speciality = set()
    symptoms = set()
    selected_symptoms = set()

    doctors = Doctor.objects.all()
    filtered_speciality_doctors = []
    filtered_symptoms_doctors = []

    for doctor in Doctor.objects.all():
        print(doctor.speciality)
        # print(doctor.symptoms.split(','))
        for symptom in doctor.symptoms.split(','):
            # print(symptom.strip())
            # symptoms.add(symptom.strip())
            if 'symptoms' in request.session and request.session['symptoms'] is not None:
                if symptom.strip() not in request.session['symptoms']:
                    symptoms.add(symptom.strip())
                else:
                    selected_symptoms.add(symptom.strip())
            else:
                symptoms.add(symptom.strip())

        if 'speciality' in request.session and request.session['speciality'] is not None:
            if doctor.speciality not in request.session['speciality']:
                specialities.add(doctor.speciality)
            else:
                selected_speciality.add(doctor.speciality)
        else:
            specialities.add(doctor.speciality)

    # print(specialities)
    # print(selected_speciality)
    # print(symptoms)
    # print(selected_symptoms)
    # print(filtered_speciality_doctors)
    # print(filtered_symptoms_doctors)

    if 'speciality' in request.session and request.session['speciality'] is not None:
        # print(request.session['speciality'])
        for doctor in doctors:
            # print(doctor)
            # print(doctor.speciality)
            # print(request.session['speciality'])
            if doctor.speciality == request.session['speciality'][0]:
                # print(doctor.speciality.split()[0])
                filtered_speciality_doctors.append(doctor)

    # print(filtered_speciality_doctors)
    # print(filtered_symptoms_doctors)

    # print('Doctors', doctors)
    # print('Filtered Doctors', filtered_speciality_doctors)

    if not filtered_speciality_doctors:
        filtered_speciality_doctors = doctors

    if 'symptoms' in request.session and request.session['symptoms'] is not None:
        # print(request.session['symptoms'])
        for doctor in filtered_speciality_doctors:
            # print(doctor)
            # print(doctor.symptoms.split(','))
            doc_symptoms = set(map(lambda x: x.strip(), doctor.symptoms.split(',')))
            patient_symptoms = set(request.session['symptoms'])
            # print(doc_symptoms)
            # print(patient_symptoms)
            if patient_symptoms.issubset(doc_symptoms):
                filtered_symptoms_doctors.append(doctor)

    # print(filtered_speciality_doctors)
    # print(filtered_symptoms_doctors)

    if not filtered_symptoms_doctors and (('symptoms' not in request.session) or (request.session['symptoms'] is None)):
        filtered_symptoms_doctors = filtered_speciality_doctors

    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'doctors': filtered_symptoms_doctors,
        'specialities': specialities,
        'selected_speciality': selected_speciality,
        'symptoms': symptoms,
        'selected_symptoms': selected_symptoms
    }

    if 'speciality' in request.session:
        del request.session['speciality']
    if 'symptoms' in request.session:
        del request.session['symptoms']

    return render(request, 'recommendations.html', context)


def index_select_doctor(request):
    # print(Doctor.objects.all())
    if request.method == "POST":
        doctor_id = request.POST['doctor']
        print(doctor_id)
        request.session['doctor_id'] = doctor_id
        print(request.session['doctor_id'])

    return redirect('/payments')


def index_filter_doctor(request):
    if request.method == "POST":
        # print(request.POST)
        # print(request.POST['speciality'])
        # print(request.POST['symptom'])

        filter_info = dict(request.POST.lists())

        # print(filter_info)

        if 'speciality' in filter_info:
            speciality = filter_info['speciality']
        else:
            speciality = None

        if 'symptoms' in filter_info:
            symptoms = filter_info['symptoms']
        else:
            symptoms = None

        # print(speciality)
        # print(symptoms)

        request.session['speciality'] = speciality
        request.session['symptoms'] = symptoms

        # print(request.session['speciality'])
        # print(request.session['symptoms'])

        return redirect('/recommendations')
