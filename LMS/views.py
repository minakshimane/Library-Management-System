from django.shortcuts import render,redirect
from LMS.models import Admin,Book
from django.contrib import messages


# Create your views here.
def index(requst):
    return render(requst,"index.html")

def adminsignup(request):
    return render(request,"adminsignup.html")

def saveadmin(request):
    email = request.POST.get("email")
    password = request.POST.get("password")
    qs=Admin.objects.filter(email=email)
    if not qs:
        Admin(email=email,password=password).save()

        return render(request,"adminsignup.html", {"message":"Thanks For Registration"})
    else:
        return render(request, "adminsignup.html", {"msg": "Email Id is already exist"})

def adminlogin(request):
    return render(request,"adminlogin.html")

def onadminlogin(request):
    em = request.POST.get("l1")
    pa = request.POST.get("l2")

    try:
        Admin.objects.get(email=em,password=pa)
        return render(request, "adminhome.html", {"name": em})
    except Admin.DoesNotExist:
        messages.error(request, "Invalid User")
        return redirect('adminlogin')

def adminhome(request):
    uname = request.GET.get("un")
    return render(request,"adminhome.html",{"name":uname})

def addbook(request):
    uname = request.GET.get("un")
    return render(request, "addbook.html", {"name": uname})

def savebook(request):
    isbn = request.POST.get("l1")
    title = request.POST.get("l2")
    author = request.POST.get('l3')
    edition = request.POST.get('l4')
    puplication = request.POST.get('l5')
    admin = request.POST.get('l6')
    uname = request.GET.get("un")
    Book(ISBN=isbn, title=title, author=author, edition=edition, publication=puplication, admin_email=admin).save()
    return render(request, "addbook.html",{"name":admin})

def bookdetail(request):
    uname = request.GET.get("un")
    stu=Book.objects.filter(admin_email=uname)

    return render(request, "bookdetail.html", {"data": stu, "name": uname})


def Book_update(request):
    uname = request.GET.get("un")

    stu = Book.objects.get(ISBN=uname,)

    return render(request, "Book_update.html", {"name": uname, "data": stu})


def update_book(request):

    i=request.POST.get("u1")
    t=request.POST.get("u2")
    a=request.POST.get("u3")
    e=request.POST.get("u4")
    p=request.POST.get("u5")
    uname=request.POST.get("un")
    una=request.POST.get("unn")
    Book.objects.filter(ISBN=una).update(ISBN=i,title=t,author=a,edition=e,publication=p)
    stu= Book.objects.filter(ISBN=una)
    return render(request,"bookdetail.html",{"data":stu,"name":uname,"message":"Information Updatated Successfully"})

def view_all(request):
    stu=Book.objects.all()
    return render(request,"view_all.html",{"data":stu})
def Book_del(request):
    uname = request.GET.get("un")
    stu = Book.objects.filter(admin_email=uname)
    return render(request, "Book_del.html", {"data": stu, "name": uname})
def Book_delete(request):
    unn = request.GET.get("mno")
    uname=request.GET.get("un")

    stu= Book.objects.filter(ISBN=unn).delete()

    return render(request, "adminhome.html", {"data": stu,"name":uname})



#  if Book.objects.filter(title=uname):

   #     Book.objects.filter(title=uname).delete()

    #else:
     #   unn = request.GET.get("un")
      #  stu = Book.objects.filter(admin_email=unn)
       # return render(request,"bookdetail.html",{"name":unn,"data":stu})



def logout(request):
    return render(request, "index.html")