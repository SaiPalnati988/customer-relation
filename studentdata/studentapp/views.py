from django.shortcuts import render,redirect
from .models import StudentData

def main_view(request):
    my_list = StudentData.objects.all()
    my_dict = {'my_list':my_list}
    return render(request,'main.html',my_dict)

def register_view(request):
    if request.method == 'GET':
        return render(request,'register.html')
    else:
        StudentData(
        name = request.POST.get('name'),
        roll_no = request.POST.get('roll_no'),
        mobile = request.POST.get('mobile'),
        institute = request.POST.get('institute'),
        location = request.POST.get('location')
        ).save()
        return redirect('mainpage')

def view_view(request,id):
    v = StudentData.objects.get(id=id)
    my_dict = {'v':v}
    return render(request,'view.html',my_dict)

def new_view(request):
    return render(request,'new.html')

def wish_view(request):
    return render(request,'wish.html')
    
