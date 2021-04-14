# VidDoc
###### OOAD SWE LAB Project PES University Sem 6 

# What is the project ?

An online doctor consultation software (similar to the Practo website).

# Components in the project

## User Authentication
###### Varun Seshu
- Django User authentication
- Secure storage of passwords (encrypted)
- Handle cases of wrong password or username
- Redirect to login in case a user is already registered

## Appointments
###### Varun Seshu
- Booking new appointments
- Select speciality and doctor
- Cancel existing appointment
- Redirect to payment/refund

## Online Consultations
###### Shashwath Kumar S
- Online consultation page
- Manage meeting link for different appointments
- Consult doctor in meeting
- Maintain prescription given by doctor

## Payments
###### Shashwath Kumar S
- Accept and authenticate payment from customer for appointment
- Refund in case of cancellation

## Recommendations
###### Hritik Shanbhag
- Search box to search for doctors by name
- Checkboxes to select symptoms
- Checkboxes to select speciality
- Reccomendation according to above criteria

## Reminders
###### Ajay
- Send email to patient’s provided email address 5 minutes before sheduled appointment time
- Send link of meeting with the email

# To build this on your computer

1. ```cd``` to the directory where you want the project to live.

2. Run these commands to initialize the project:

```
git clone "git@github.com:Varun487/VidDoc.git"

cd VidDoc

pip3 install -r requirements.txt

pyhton3 VidDoc/manage.py runserver
```
3. To migrate changes to the database:
```
python3 VidDoc/manage.py makemigrations

python3 VidDoc/manage.py migrate
```
4. Create a superuser for the database:
```
python3 VidDoc/manage.py createsuperuser
```

# Project Members
###### All project members are from PES University EC Campus Semester 6 Section E

1. Varun Seshu - PES2201800074
2. Shashwath S Kumar - PES2201800623 
3. Hritik Shanbhag - PES2201800082
4. Ajay - PES2201800724

# TODO
### To be completed before 15th April
- Explain all work done  ![INCOMPLETE](https://img.shields.io/badge/MEETING-INCOMPLETE-orange)
- Fix all diagrams and documents  ![INCOMPLETE](https://img.shields.io/badge/DOC-INCOMPLETE-orange)
- Automated Testing  ![INCOMPLETE](https://img.shields.io/badge/FEATURE-INCOMPLETE-orange)
- AUTHENTICATION ![FEATURE](https://img.shields.io/badge/FEATURE-INPROGRESS-yellow)
  - Login ![DONE](https://img.shields.io/badge/DONE-brightgreen)
    - Enter site if user exists ![DONE](https://img.shields.io/badge/DONE-brightgreen)
    - Mention if any required fields not filled ![DONE](https://img.shields.io/badge/DONE-brightgreen)
    - Mention if user not registered ![DONE](https://img.shields.io/badge/DONE-brightgreen)
    - Mention if wrong password ![DONE](https://img.shields.io/badge/DONE-brightgreen)
    - If remember me is checked, redirect to site next time ![DONE](https://img.shields.io/badge/DONE-brightgreen)
    - If remember me is not checked, expire cookie at browser window close ![DONE](https://img.shields.io/badge/DONE-brightgreen)
  - Register ![DONE](https://img.shields.io/badge/DONE-brightgreen)
    - Redirect to login after successful registration ![DONE](https://img.shields.io/badge/DONE-brightgreen)
    - Mention if ![DONE](https://img.shields.io/badge/DONE-brightgreen)
      - Any required fields not filled ![DONE](https://img.shields.io/badge/DONE-brightgreen)
      - Username not available ![DONE](https://img.shields.io/badge/DONE-brightgreen)
      - Wrong email format ![DONE](https://img.shields.io/badge/DONE-brightgreen)
      - Email already registered ![DONE](https://img.shields.io/badge/DONE-brightgreen)
      - Password not matching ![DONE](https://img.shields.io/badge/DONE-brightgreen)
      - Age not correct ![DONE](https://img.shields.io/badge/DONE-brightgreen)
      - Phone number not correct ![DONE](https://img.shields.io/badge/DONE-brightgreen)
    - Not able to get correct address information ![DONE](https://img.shields.io/badge/BUG-red)
    - Write tests  ![INCOMPLETE](https://img.shields.io/badge/INCOMPLETE-orange)
- Complete appointments ![DONE](https://img.shields.io/badge/FEATURE-INCOMPLETE-red)
  - List all upcoming appointments for a user  ![INCOMPLETE](https://img.shields.io/badge/INCOMPLETE-orange)
  - Button for Booking new appointments
  - Page with form for appointment
    - Redirects to recommendations of doctors selecting speciality and symptoms
    - Redirects to payments
    - Fix Data consistency across all pages
    - Fix appointment booking confirmation across payment
  - Cancel existing appointment
    - Redirects to refund
    - Fix Data consistency across all pages
    - Fix appointment booking confirmation across payment
- Complete Consultations  ![DONE](https://img.shields.io/badge/FEATURE-INCOMPLETE-red)
- Complete payments  ![DONE](https://img.shields.io/badge/FEATURE-INCOMPLETE-red)
- Complete Recommendations  ![DONE](https://img.shields.io/badge/FEATURE-INCOMPLETE-red)
- Complete email reminders  ![DONE](https://img.shields.io/badge/FEATURE-INCOMPLETE-red)
- Complete test plan document  ![DONE](https://img.shields.io/badge/DOC-INCOMPLETE-red)
- Complete final report  ![DONE](https://img.shields.io/badge/DOC-INCOMPLETE-red)
