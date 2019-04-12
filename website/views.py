from django.shortcuts import render, redirect
from website.forms import*
from blog import settings
from django.core.mail import send_mail


# Create your views here.
def home(request):
        return render(request,'home.html')



def detail(request):
        return render(request,'detail.html')




def send(request):
    if request.method=='POST':
        fm=sendmail(request.POST)
        if fm.is_valid():
            to=fm.cleaned_data['to']
            sub=fm.cleaned_data['subject']
            msg=fm.cleaned_data['body']
            res=send_mail(sub,msg,settings.EMAIL_HOST_USER,[to])
            if(res==1):
                msg='Mail sent Successfully'
            else:
                msg='mail couldnt send'
        return redirect('/email')
    else:
        fm=sendmail()
    return render(request,'mail.html',{'fm':fm})




def blog(request):
        return render(request,'blog.html')



def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect("/show")  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form})  

def show(request):  
    employees = Employee.objects.all()  
    return render(request,"show.html",{'employees':employees})  
def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  
def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})  
def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")  
def home(request):
    return render(request,'home.html')



#####################################################





