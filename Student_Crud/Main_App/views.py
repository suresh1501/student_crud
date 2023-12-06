from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm, LoginForm
from django.contrib.auth import authenticate, login
from .models import Student_Details
from django.contrib.auth.decorators import login_required

def Login(request):
    if request.method == 'GET':
        context = {}
        context['form'] = LoginForm()
        return render(request, 'Login.html', context)
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/list')
            else:
                return redirect('/login')

@login_required(login_url='/login')
def List(request):
    all_values = Student_Details.objects.all()
    return render(request, 'Student_List.html', {'table_values' : all_values})

@login_required(login_url='/login')
def Student_Entry_Form(request):
    form = StudentForm()
    return render(request, 'Student_Details_Entry_Form.html', {'form' : form})

@login_required(login_url='/login')
def Insert_db(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        roll_no = form.cleaned_data['roll_no']
        name = form.cleaned_data['name']
        age = form.cleaned_data['age']
        city = form.cleaned_data['city']
        print(roll_no, name, age, city)
        context = Student_Details(roll_no=roll_no, name=name, age=age, city=city)
        context.save()
        return redirect('/list')

@login_required(login_url='/login')
def Edit(request, id=None):
    if id == None:
        return redirect('/list')
    else:
        student_value = get_object_or_404(Student_Details, id=id)
        if request.method == 'GET':
            context = {'form': StudentForm(instance=student_value), 'id': id }
            return render(request, 'Student_Details_Entry_Form.html', context)
        elif request.method == 'POST':
            form = StudentForm(request.POST, instance=student_value)
            if form.is_valid():
                form.save()
                return redirect('/list')
            else:
                return render(request, 'Student_Details_Entry_Form.html', {'form': form})
    
@login_required(login_url='/login')
def Delete(request, id):
    if id == None:
        return redirect('/list')
    else:
        del_id = Student_Details.objects.get(id=id)
        del_id.delete()
        return redirect('/list')