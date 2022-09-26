from django.shortcuts import render,HttpResponseRedirect
from .form import StudentRegistration
from .models import User


# Create your views here.
#this function will add new item and show new item
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            fm = StudentRegistration()

    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/add&show.html', {'form': fm, 'stu': stud})

# this function will edit and update
def update(request, id):
    if request.method == "POST":
        u = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=u)
        if fm.is_valid:
            fm.save()
    else:
        u = User.objects.get(pk=id)
        fm = StudentRegistration(instance=u)
    return render(request, 'enroll/edit.html', {'form':fm})



#this function will delete data
def delete(request, id):
    if request.method == "POST":
        d = User.objects.get(pk=id)
        d.delete()
        return HttpResponseRedirect('/')

