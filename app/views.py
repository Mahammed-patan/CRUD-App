from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def Insertdataview(request):
    return render(request,'app\insert.html')

def insertData(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    contact = request.POST['contact']

    newuser = Student.objects.create(Firstname=fname,Lastname=lname,
                                        Email=email,Contact=contact)

    return redirect('showpage')


def showpage(request):
    all_data = Student.objects.all()
    return render(request,'app\show.html',{'key1':all_data})


def Editpage(request,pk):
    get_data = Student.objects.get(id=pk)
    return render(request,'app\edit.html',{'key2':get_data})


def UpdateData(request,pk):
    udata = Student.objects.get(id=pk)
    udata.Firstname = request.POST['fname']
    udata.Lastname = request.POST['lname']
    udata.Email = request.POST['email']
    udata.Contact = request.POST['contact']
    udata.save()
    return redirect('showpage')

def DeleteData(request,pk):
    d_data = Student.objects.get(id=pk)
    d_data.delete()
    return redirect('showpage')