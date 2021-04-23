from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from django.shortcuts import render,redirect

from app.models import Employee1
from app.forms import EmployeeForm1



# Create your views here.
def show(request):
    employees=Employee1.objects.all()
    return render(request,'app/index.html',{'employees':employees})
def display(request):
    #form=EmployeeForm()
    if request.method=='POST':
        employeeid=request.POST['id']
        name=request.POST['name']
        phone=request.POST['phone']
        age=request.POST['age']
        email=request.POST['email']
        if employeeid=='' or name=='' or phone=='' or email=='' or age=='':
            messages.info(request,'fill all details')
            return redirect('/')
        else:
            form=Employee1.objects.create(empid=employeeid,name=name,phone=phone,email=email,age=age)
            form.save();
        return redirect('/')
    return render(request,'app/index.html')


def delete(request,id):
    employee=Employee1.objects.get(id=id)
    employee.delete()
    employees=Employee1.objects.all()
    return render(request,'app/index.html',{'employees':employees, 'res':'true', 'msg':'Deleted ', 'classStyle':"alert "})

def update(request,id):
    employee=Employee1.objects.get(id=id)
    if request.method=='POST':
        form=EmployeeForm1(request.POST ,instance=employee)
        if form.is_valid():
            form.save()
            
            return render(request,'app/update.html',{'employee':employee,'res':'true','msg':' values updated ', 'classStyle':"alert alert-dark"})
           
        else:
     
            return render(request,'app/update.html',{'employee':employee,'res':'false', 'msg':'Invalid', 'classStyle':'alert alert-dark'})
            
    else:
        return render(request,'app/update.html',{'employee':employee,'res':'false'})
