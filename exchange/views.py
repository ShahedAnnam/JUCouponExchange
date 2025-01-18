from django.shortcuts import HttpResponse
from django.shortcuts import render,redirect
from .models import Student



def home(request):
    return render(request,'home.html')


def form(request):
    return render(request,'form.html')


def loginForm(request):

    if request.method == 'POST':
        batch = request.POST.get('batch')
        roll = request.POST.get('roll')

        students = Student.objects.filter(batch=batch, roll=roll)

        if students.exists():
            
            return redirect('list') 
        else:
            error_message = "No matching records found. Please check your batch and roll number"
            return render(request, 'loginForm.html', {'error_message': error_message})

    return render(request,'loginForm.html')



def saveInfo(request):
    if request.method=='POST':
        name = request.POST.get('name')
        dept = request.POST.get('dept')
        batch = request.POST.get('batch')
        roll = request.POST.get('roll')
        number = request.POST.get('number')
        message = request.POST.get('message', '') 
        allotedHall = request.POST.get('allotedHall')
        desiredHall = request.POST.get('desiredHall')

        student = Student(
            name=name,
            dept=dept,
            batch=batch,
            roll=roll,
            number=number,
            message=message,
            allotedHall=allotedHall,
            desiredHall=desiredHall
        )
        student.save()

    successMessage = "Successfully registerd,your record is saved, login to see the coupon exhcange list"

    return render(request,'loginForm.html',{'successMessage': successMessage})


def list(request):
    alloted_hall_filter = request.GET.get('allotedHall',None)
    desired_hall_filter = request.GET.get('desiredHall',None)

    # Fetch all students from the database
    students = Student.objects.all()

    if alloted_hall_filter:
        students = students.filter(allotedHall=alloted_hall_filter)
    if desired_hall_filter:
        students = students.filter(desiredHall=desired_hall_filter)

    return render(request, 'list.html', {'students': students})


def about(request):
    return render(request,'index.html')

