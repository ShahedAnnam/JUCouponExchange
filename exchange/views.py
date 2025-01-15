from django.shortcuts import HttpResponse
from django.shortcuts import render
from .models import Student



def home(request):
    return render(request,'index.html')



def list(request):
    if request.method=='POST':
        name = request.POST.get('name')
        dept = request.POST.get('dept')
        batch = request.POST.get('batch')
        number = request.POST.get('number')
        message = request.POST.get('message', '') 
        allotedHall = request.POST.get('allotedHall')
        desiredHall = request.POST.get('desiredHall')

        student = Student(
            name=name,
            dept=dept,
            batch=batch,
            number=number,
            message=message,
            allotedHall=allotedHall,
            desiredHall=desiredHall
        )
        student.save()
    return render(request,'list.html',{'message':'form submitted successfully'})



def about(request):
    return render(request,'index.html')

