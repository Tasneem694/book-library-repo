from django.shortcuts import render
from admn.models import registers,books
from django.http import HttpResponseRedirect
from .form import *
from datetime import datetime
# Create your views here.

def students(req):
    students=registers.objects.filter(is_admin=False)
    ctxt={}
    ctxt['stds']=students
    if (req.method == 'POST'):
        std=registers.objects.filter(id=req.POST['search'])
        ctxt['search_std']=std
        return render(req, 'search student.html', ctxt)
    return render(req,'students.html',ctxt)

def details(req,ID):
    stdet=registers.objects.filter(id=ID)
    contxt={}
    contxt['stds']=stdet
    return render(req,'details.html',contxt)

def delete_student(req,ID):
    registers.objects.get(id=ID).delete()
    return HttpResponseRedirect('/students')

def update_student(req,ID):
    std = registers.objects.filter(id=ID)[0]
    form = UpdateStudent(instance=std)
    context = {}
    if (req.method == 'POST'):
        frm = UpdateStudent(req.POST, instance=std)
        if (frm.is_valid()):
            frm.save()  # act as update
            return HttpResponseRedirect('/students')
        else:
            context['msg'] = 'invalid data'
    context['update_form'] = form
    return render(req, 'update student.html', context)

def std_books(req):
    # time_now = datetime.datetime.now()
    # print(time_now)
    boks=books.objects.all()
    contxt={}
    contxt['book']=boks
    if (req.method == 'POST'):
        bok=books.objects.filter(book_id=req.POST['search'])
        contxt['search_book']=bok
        return render(req, 'search book.html', contxt)
    return render(req, 'std books.html',contxt)

def book_details(req,ID):
    bok=books.objects.filter(book_id=ID)
    contxt={}
    contxt['book_details']=bok
    return render(req,'book details.html',contxt)

def std_borrowd(req):
    bok=books.objects.filter(is_borrowed=True)
    contxt={}
    contxt['std_borrowd']=bok
    return render(req,'std borrowed.html',contxt)

def update_borrow(req,ID):
        # time_now=datetime.strftime(,'%I:%M %p') #strftime('%Y-%m-%d %I:%M %p')
        bok = books.objects.filter(book_id=ID)[0]
        form = UpdateBorrow(instance=bok)
        context = {}
        if (req.method == 'POST'):
            frm = UpdateBorrow(req.POST, instance=bok)
            # if (frm.is_valid()):
            #     print(req.POST)
            frm.save()  # act as update
            if(bok.is_borrowed==True):
                bok=books.objects.filter(book_id=ID).update()
            else:
                bok=books.objects.filter(book_id=ID).update(retrn_dt=None)
                bok=books.objects.filter(book_id=ID).update(borow_dt=None)


            return HttpResponseRedirect('/std_books')
            # else:
            #     context['msg'] = 'invalid data'
        context['update_form'] = form
        context['book_name'] = bok.book_name
        context['borrow_dt'] = bok.borow_dt
        context['return_dt'] = bok.retrn_dt

        return render(req, 'update borrow.html', context)


