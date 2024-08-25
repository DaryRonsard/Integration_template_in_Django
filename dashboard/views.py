from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.




#def index(request):
# return HttpResponse("<h1>Hello, world. You're welcome.</h1>")
def index(request):
 return render(request, 'dashboard/index.html')