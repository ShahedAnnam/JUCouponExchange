from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from .models import Student
from django.contrib import messages



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
            student = students.first()
            request.session['is_authenticated'] = True 
            request.session['roll'] = roll  
            request.session['batch'] = batch 
            return render(request, 'loginForm.html', {'student': student})
        else:
            messages.error(request, "No matching records found. Please check your batch and roll number or if not registed yet,then register first")

    return render(request,'loginForm.html')


def logout(request):
    request.session.flush() 
    return redirect('loginForm')




def delete_request(request):
    batch = request.session.get('batch')
    roll = request.session.get('roll')


    deleted_count, _ = Student.objects.filter(batch=batch, roll=roll).delete()
    if deleted_count > 0:
        messages.success(request, "Your records have been successfully deleted.")
        logout(request)
    else:
        messages.error(request, "No matching records found to delete.")

    return redirect('loginForm') 


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

    messages.success(request, "Successfully registerd,your record is saved, login to see the coupon exhcange list")
    return render(request,'loginForm.html')
    


def list(request):

    
    alloted_hall_filter = request.GET.get('allotedHall',None)
    desired_hall_filter = request.GET.get('desiredHall',None)

    # Fetch all students from the database
    students = Student.objects.all()

    if alloted_hall_filter:
        students = students.filter(allotedHall=desired_hall_filter)
    if desired_hall_filter:
        students = students.filter(desiredHall=alloted_hall_filter)

        
    if not request.session.get('is_authenticated'):
        return render(request, 'list.html', {'is_blurred': True,'students': students})

    return render(request, 'list.html', {'students': students})


def about(request):
    return render(request,'about.html')

