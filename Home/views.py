from django.shortcuts import render

# Create your views here.

def home(request):
    context = {
        'title':'HOME',
    }
    return render(request,'Home/home.html',context)