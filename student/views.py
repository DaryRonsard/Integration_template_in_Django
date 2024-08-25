from django.http import HttpResponse
from django.shortcuts import render
from student.forms import StudentForm


# Create your views here.
#def index(request):
#    return render(request, 'index.html')

def index(request):
    #    return HttpResponse("<h1>Hello World</h1>")
    eleve={
        'name':'dary',
        'email':'hiendary',
    }
    form = StudentForm()
    return render(request, 'student/index.html', context={'eleve':eleve,'form':form})

def add(request):
    form = StudentForm()
    return  render(request, "student/ajoueEleve.html", {'form':form})
def edit(request):
    return  render(request, "student/modifieEleve.html")
