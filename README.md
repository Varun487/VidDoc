# VidDoc
###### OOAD SWE LAB Project PES University Sem 6 

# What is the project ?

An online doctor consultation software (similar to the Practo website).

# Components in the project

## User Authentication
###### Varun Seshu and Ajay
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
###### Varun Seshu and Hritik Shanbhag 
- Search box to search for doctors by name
- Checkboxes to select symptoms
- Checkboxes to select speciality
- Reccomendation according to above criteria

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
- Complete test plan document  ![DOCCOMPLETE]
- AUTHENTICATION ![FEATURECOMPLETE]
  - Login ![DONE]
    - Enter site if user exists ![DONE]
    - Mention if any required fields not filled ![DONE]
    - Mention if user not registered ![DONE]
    - Mention if wrong password ![DONE]
    - If remember me is checked, redirect to site next time ![DONE]
    - If remember me is not checked, expire cookie at browser window close ![DONE]
  - Register ![DONE]
    - Redirect to login after successful registration ![DONE]
    - Mention if ![DONE]
      - Any required fields not filled ![DONE]
      - Username not available ![DONE]
      - Wrong email format ![DONE]
      - Email already registered ![DONE]
      - Password not matching ![DONE]
      - Age not correct ![DONE]
      - Phone number not correct ![DONE]
    - Not able to get correct address information ![BUGFIXED]
- APPOINTMENTS ![FEATURECOMPLETE]
  - List all upcoming appointments for a user  ![DONE]
  - Button for Booking new appointments  ![DONE]
  - Page with form for appointment  ![DONE]
    - Redirects to recommendations of doctors selecting speciality and symptoms  ![DONE]
    - Redirects to payments  ![DONE]
    - Fix Data consistency across all pages  ![DONE]
    - Fix appointment booking confirmation after payment  ![DONE]
  - Button for Cancelling existing appointments  ![DONE]  
  - Cancel existing appointment dialogue box  ![DONE]
- Complete Payments  ![FEATURECOMPLETE]
    - Create payment form with phone number and OTP ![DONE]
    - Update appointment data for the user ![DONE]
- Complete Consultations  ![FEATUREINCOMPLETE]
    - List all upcoming appointments and previous consultation ![INCOMPLETE]
    - Create prescriptions for consultations ![INCOMPLETE]
    - Add meeting link for upcoming appointments ![INCOMPLETE]
- Complete Recommendations  ![FEATUREINCOMPLETE]
- Complete Final submission ![DOCINCOMPLETE]
  - Folder in Drive ![INCOMPLETE]
  - Submission in Edmodo ![INCOMPLETE]
- Automated Testing  ![FEATUREINCOMPLETE]
    - Set up selenium automated testing ![DONE]
    - Write 10 tests for Authentication  ![DONE]
    - Write 10 tests for Appointments ![INCOMPLETE]
    - Write 10 tests for Consultations ![INCOMPLETE]
    - Write 10 tests for Payments ![INCOMPLETE]
    - Write 10 tests for Recommendations ![INCOMPLETE]
    - Write 10 tests for Email Reminders ![INCOMPLETE]
- CSS and final touches for the website ![FEATUREINCOMPLETE]

[DONE]: https://img.shields.io/badge/DONE-brightgreen
[INCOMPLETE]: https://img.shields.io/badge/INCOMPLETE-red
[BUGFIXED]: https://img.shields.io/badge/BUG-FIXED-brightgreen
[FEATUREINCOMPLETE]: https://img.shields.io/badge/FEATURE-INCOMPLETE-red
[FEATURECOMPLETE]: https://img.shields.io/badge/FEATURE-COMPLETE-brightgreen
[MEETINGINCOMPLETE]: https://img.shields.io/badge/MEETING-INCOMPLETE-red
[DOCINCOMPLETE]: https://img.shields.io/badge/DOC-INCOMPLETE-red
[DOCCOMPLETE]: https://img.shields.io/badge/DOC-COMPLETE-brightgreen
