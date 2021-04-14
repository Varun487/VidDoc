from django.shortcuts import render, redirect
from .models import User
import hashlib
import re


def login_required(func):
    def inner(*args, **kwargs):
        if 'user_id' in args[0].session:
            return func(*args, **kwargs)
        else:
            return redirect('/login')

    return inner


def index_login(request):
    # print(request.session.keys())

    if 'user_id' in request.session.keys():
        return redirect('/appointments')

    context = {
        "try_again": False,
        "not_registered": False
    }

    return render(request, 'login.html', context)


def index_logout(request):
    if 'user_id' in request.session.keys():
        del request.session['user_id']
    return redirect('/login')


def index_register(request):
    context = {
        "invalid_user": False,
        "valid_email": True,
        "valid_password": True,
        "valid_age": True,
        "valid_phone_number": True
    }

    return render(request, 'register.html', context)


def auth_login(request):
    if request.method == "POST":
        name = request.POST['name']
        password = request.POST['password']

        # print(request.POST)

        if 'remember' not in request.POST:
            # print('expiry set to 0')
            request.session.set_expiry(0)

        # print('name: ', name)
        # print('password: ', password)
        # print('sha256 of password: ', hashlib.sha256(password.encode()).hexdigest())

        authorised = User.objects.filter(name=name, password=hashlib.sha256(password.encode()).hexdigest())
        not_registered = not User.objects.filter(name=name)

        # print(authorised)
        # print(not_registered)

        if authorised:
            request.session['user_id'] = authorised[0].id
            return redirect('/appointments')

        elif not_registered:
            context = {
                "try_again": False,
                "not_registered": True
            }

            return render(request, 'login.html', context)

        else:
            context = {
                "try_again": True,
                "not_registered": False
            }

            return render(request, 'login.html', context)


def auth_register(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        repeat_password = request.POST['repeat_password']
        address = request.POST['address']
        age = request.POST['age']
        city = request.POST['city']
        phone_number = request.POST['phone_number']

        # print('name: ', name)
        # print('email: ', email)
        # print('password: ', password)
        # print('sha256 of password: ', hashlib.sha256(password.encode()).hexdigest())
        # print('Repeat password: ', repeat_password)
        # print('sha256 of Repeat password: ', hashlib.sha256(repeat_password.encode()).hexdigest())
        # print('address: ', address)
        # print('age: ', age)
        # print('type age: ', type(age))
        # print('age: ', int(age))
        # print('type age: ', type(int(age)))
        # print('city: ', city)
        # print('Phone number: ', phone_number)
        # print('type Phone number: ', type(phone_number))
        # print('Phone number: ', int(phone_number))
        # print('type Phone number: ', type(int(phone_number)))
        # print('datetime:', date)

        invalid_user = User.objects.filter(name=name)
        valid_email = re.match(r"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$", email) is not None
        valid_password = password == repeat_password
        valid_age = 0 <= int(age) <= 130
        valid_phone_number = len(phone_number) == 10

        # print('Invalid user:', not invalid_user)
        # print('Valid email:', valid_email)
        # print('Valid password:', valid_password)
        # print('Valid age:', valid_age)
        # print('Valid phone number:', valid_phone_number)

        authorised = (not invalid_user) and valid_email and valid_age and valid_password and valid_phone_number

        # print(authorised)

        if authorised:

            # Create new user object and save to database
            User(
                name=name,
                email=email,
                password=hashlib.sha256(password.encode()).hexdigest(),
                address=address,
                age=int(age),
                city=city,
                phone_number=int(phone_number)
            ).save()

            return redirect('/login')

        else:
            context = {
                "invalid_user": invalid_user,
                "valid_email": valid_email,
                "valid_password": valid_password,
                "valid_age": valid_age,
                "valid_phone_number": valid_phone_number
            }

            return render(request, 'register.html', context)
