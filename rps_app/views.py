from django.shortcuts import render
from .models import *
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
def info(request):
    print("hlo info")
    
    return render(request,'info.html')
def play(request):
    myname=""
    if(request.method=='POST'):
        sname=request.POST.get('sname')
        roll=request.POST.get('roll')

        submit=Info(sname=sname,roll=roll)
        myname=sname
        submit.save()
    context={'name':myname}
    print(myname)
    return render(request,'play.html',context=context)

def end(request):
    if(request.method=='POST'):
        score=request.POST.get('u_score')
        result=request.POST.get('result')
        
        submit=Info(sname=score,roll=result)
        print(score,result,"helo")
        submit.save()
    data=Info.objects.all()
    context={"data":data}
    return render(request,'end.html',context=context)
