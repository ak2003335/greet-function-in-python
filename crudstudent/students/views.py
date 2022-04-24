
from django.http import HttpResponse
from django.shortcuts import redirect, render
from students.forms import StudentForms
from students.models import Student

from students.forms import StudentForms

# Create your views here.
def add(request):
    print("in stu funcaton is calling ")
    if request.method == 'POST':
        print("Inside POST Methord  ")
        form = StudentForms(request.POST)
        print("Inside POST Methord request ")
        if form.is_valid():
            print(">>>> valid  ")
            form.save()
            print(">>>> save  ")
            return redirect('/show')
    form=StudentForms()
    return render(request,'index.html',{'form': form})




def show(request):
    students = Student.objects.all()
    return render(request,'show.html',{'students':students})


#Edit Function

def edit(request,id):
    student =Student.objects.get(id=id)

    return render(request,'edit.html',{'student':student})

#Login function
def login(request):
    return render(request,'login.html')

def delete(request,id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect(request,'show.html')

