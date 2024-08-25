from django.shortcuts import render
from .forms import LoginForm

# Create your views here.
def index(request):
    form = LoginForm()
    return render(request, 'login/index.html', {'form': form})

#def Login(request):
#    form = LoginForm()
#    return render(request, "login/index.html", context={"form": form})