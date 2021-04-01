from django.shortcuts import render

# Create your views here.
def consult(request):

    return render(request, 'consultation.html')
