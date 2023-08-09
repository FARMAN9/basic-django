from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/home/')
def homepage(resquest):
    context={'page':'homepage'}
    return render(resquest ,'home.html',context)
@login_required(login_url='/adddata/')
def adddata(resquest):
    context={'page':'adddata'}
    if resquest.method=='POST':
        data=resquest.POST
        name=data.get('name')
        roll=data.get('roll')
        age=data.get('age')
        address=data.get('address')
        phone=data.get('phone')
        email=data.get('email')
        photo=resquest.FILES.get('photo')
        myobj={'name':name,'roll':roll,'age':age,'address':address,'phone':phone,'email':email,'photo':photo}
        Student.objects.create(**myobj)
        saved='data saved'
        context={'save':saved}
        #return ("/adddata/",context)
    return render(resquest ,'adddata.html',context)
@login_required(login_url='/updatadata/')
def updatedata(resquest):
    context={'page':updatedata}
    if  resquest.GET.get('search'):
        
        try:
            QuerySet=Student.objects.filter(roll=resquest.GET.get('search')) 
            context={"Students":QuerySet,'x':resquest.GET.get('search')}
            idget=Student.objects.get(roll=resquest.GET.get('search')) 
            context={"Students":QuerySet,'x':resquest.GET.get('search'),'S':idget}
        except:
            Exception       
    if resquest.method=='POST':
        idget=Student.objects.get(roll=resquest.GET.get('search')) 
        id=idget.id
        print(id)
        d=Student.objects.get(id=id)
        
        data=resquest.POST
        name=data.get('name')
        roll=data.get('roll')
        age=data.get('age')
        address=data.get('address')
        phone=data.get('phone')
        email=data.get('email')
        photo=resquest.FILES.get('photo')
        d.name=name
        d.roll=resquest.GET.get('search')
        d.address=address
        d.age=age
        d.phone=phone
        d.email=email
        d.photo=photo
        d.save()
        saved='updataed '
        idget={}
        context={'save':saved,'Students':QuerySet,'x':'','S':idget}
    return render(resquest,'updatedata.html',context)
@login_required(login_url='/finddata/')
def finddata(resquest):
    context={'page':'adddata'}
    if resquest.GET.get('search')or resquest.GET.get('nameS'):
        x= resquest.GET.get('search')
        if x==' ':
            error='empty provide key'
            context={'error':error}
            print(error,x)
        elif resquest.GET.get('search'):
            QuerySet=Student.objects.filter(roll=x)
            print(QuerySet)
            context={'Students': QuerySet}
        else:
            QuerySet=Student.objects.filter(name__icontains=resquest.GET.get('nameS'))
            print(QuerySet)
            context={'Students': QuerySet}    
        print( resquest.GET.get('search'))
        print( resquest.GET.get('nameS'))
    return render(resquest,'finddata.html',context)
def deletedata(resquest):
    return HttpResponse("deleted")
@login_required(login_url='/showdata/')
def showdata(resquest):
    QuerySet=Student.objects.all()
    context={'Students':QuerySet}
    context2={'page':'showdata'}
    return render(resquest,'showdata.html',context)
@login_required(login_url='/deleteS/')
def deleteS(resquest,id):
    d=Student.objects.get(id=id)
    d.delete()
    return redirect('/showdata/')#removed resquest
def reg(resquest):
    if resquest.method != 'POST':
        return render(resquest,'reg.html')
    first_name=resquest.POST.get('first_name')
    last_name=resquest.POST.get('last_name')
    username=resquest.POST.get('username')
    password=resquest.POST.get('password')
    password2=resquest.POST.get('password2')
    user=User.objects.filter(username=username)
    if user.exists():
        messages.info(resquest,'Username already taken')
        return redirect('/reg/')
    if password != password2:
        print("mismatch conf password")
        messages.info(resquest,'conform password missmatch')
    else:
        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        user.set_password(password)
        user.save()
        messages.info(resquest,'Account created successfuly')
    return redirect('/reg/')
    
def loginx(resquest):
     if resquest.method=='POST':
        username=resquest.POST.get('username')
        password=resquest.POST.get('password')
        user=User.objects.filter(username=username)
        if user.exists():
            user=authenticate(username=username,password=password)
            if user is None:
                messages.info(resquest,'invalid username or password')
                return redirect('/')
            else:
                login(resquest,user)
                return redirect('/home/')
        else:
            messages.info(resquest,'invalid username or password')        
     return render(resquest,'login.html')
@login_required(login_url='/logout/')
def logoutx(resquest):
    logout(resquest)
    return redirect('/')

