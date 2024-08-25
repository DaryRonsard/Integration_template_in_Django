from django.shortcuts import render

from teacher.forms import TeacherForm


# Create your views here.
def index(request):
    form = TeacherForm()
    return render(request, 'user/utilisateur.html', context={"form": form})


#def User(request):
     #form = UserForm
#    return render(request, 'user/utilisateur.html', )


