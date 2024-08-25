from django.shortcuts import render
from teacher.forms import TeacherForm
# Create your views here.

#def index(request):
#    form = TeacherForm()
#    return render(request, 'professeur/professeur.html')

def index(request):
    form = TeacherForm()
    return render(request, 'professeur/professeur.html', context={"form": form})