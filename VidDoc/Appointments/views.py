from django.shortcuts import render
from UserAuthentication.views import login_required


@login_required
def index_appointments(request):
    # print(request.session)
    return render(request, 'appointments.html')
