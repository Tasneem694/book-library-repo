from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from .form import *
import sys
# Create your views here.
def home(req):
    return render(req,'home.html')


def login(req):
    contxt={}
    if(req.method == 'POST'):
        obj=registers.objects.filter(email=req.POST['email'],password=req.POST['passwrd'])
        if(len(obj)>0):
            req.session['id']=obj[0].id
            req.session['name']=obj[0].name
            req.session['is_admin']=obj[0].is_admin
            return HttpResponseRedirect('/')
        else:
           contxt['msg']='invalid email or password !'
    return render(req,'login.html',contxt)

def logout(req):
    req.session.clear()
    req.session.flush()
    return HttpResponseRedirect('/login')


def register(req):
    context={}
    reg = registers()
    if(req.method=='POST'):
            regs=registers.objects.filter(email=req.POST['email'])
            if(len(regs)>0):
                context['error1']='This email is already used, Please try another account'
            else:
                reg.name = req.POST['name']
                reg.email = req.POST['email']
                if(req.POST['confpass']== req.POST['passwrd']):
                    reg.password = req.POST['passwrd']
                    reg.save()
                    return HttpResponseRedirect('/login')
                elif(req.POST['confpass'] != req.POST['passwrd']):
                    context['error0']='password and password confirmation are not equal'

    return render(req,'sign up.html',context)

def users(req):
    print(req.POST)
    users=registers.objects.all()
    contxt={}
    contxt['users']=users
    if (req.method == 'POST'):
        user=registers.objects.filter(id=req.POST['search'])
        contxt['search_user']=user
        return render(req, 'search user.html', contxt)

    return render(req,'users.html',contxt)

def add_user(req):
    contxt={}
    usrform=UpdateUser()
    if(req.method=='POST'):
        # print(req.session)
        usrform=UpdateUser(req.POST)
        # print(req.POST)
        if(usrform.is_valid()):
                usrform.save()
                return HttpResponseRedirect('/users')
        else:
            contxt['msg']='inserted data invalid, try again'
    usrform = UpdateUser()
    contxt['add_user']=usrform
    return render(req, 'add user.html',contxt)

def delete_user(req,ID):
    registers.objects.filter(id=ID).delete()
    return HttpResponseRedirect('/users')

def update_user(req,ID):
    usr = registers.objects.filter(id=ID)[0]
    form = UpdateUser(instance=usr)
    context = {}
    if (req.method == 'POST'):
        frm = UpdateUser(req.POST, instance=usr)
        if (frm.is_valid()):
            frm.save()  # act as update
            return HttpResponseRedirect('/users')
        else:
            context['msg'] = 'invalid data'
    context['update_form'] = form
    return render(req, 'update user.html', context)

def view_books(req):
    boks=books.objects.all()
    contxt={}
    contxt['book']=boks
    if (req.method == 'POST'):
        bok=books.objects.filter(book_id=req.POST['search'])
        contxt['search_book']=bok
        return render(req, 'search book.html', contxt)
    return render(req, 'books.html',contxt)

def delete_book(req,ID):
    books.objects.filter(book_id=ID).delete()
    return HttpResponseRedirect('/view_books')

def update_book(req,ID):
    bok = books.objects.filter(book_id=ID)[0]
    form = UpdateBook(instance=bok)
    context = {}
    if (req.method == 'POST'):
        frm = UpdateBook(req.POST, instance=bok)
        if (frm.is_valid()):
            frm.save()  # act as update
            return HttpResponseRedirect('/view_books')
        else:
            context['msg'] = 'invalid data'
    context['update_form'] = form
    return render(req, 'update book.html',context)

def add_book(req):
    contxt={}
    bokform=NewBook()
    if(req.method=='POST'):
        # print(req.session)
        bokform=NewBook(req.POST)
        # print(req.POST)
        if(bokform.is_valid()):
                bokform.save()
                return HttpResponseRedirect('/view_books')
        else:
            contxt['msg']='inserted data invalid, try again'
    bokform = NewBook()
    contxt['add_book']=bokform
    return render(req, 'add book.html',contxt)

def borrowed_books(req):
    boks=books.objects.filter(is_borrowed=True)
    contxt={}
    contxt['borrowed_books']=boks
    return render(req, 'borrowed books.html',contxt)

def profile(req):
    person = registers.objects.filter(id=req.session['id'])[0]
    form = UpdateUser(instance=person)
    context = {}
    if (req.method == 'POST'):
        frm = UpdateUser(req.POST, instance=person)
        if (frm.is_valid()):
            frm.save()  # act as update
            return HttpResponseRedirect('/login')
        else:
            context['msg'] = 'invalid data'
    context['update_form'] = form
    return render(req, 'profile.html', context)



