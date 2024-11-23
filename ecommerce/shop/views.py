from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from shop.models import Category,Product
# Create your views here.



def categories(request):
    c=Category.objects.all()
    context={'category':c}
    return render(request,'categories.html',context)

def products(request,p):  #here p receives the category id
    # print(p)
    c=Category.objects.get(id=p)   #reads a particular category object using id
    p=Product.objects.filter(category=c)  #reads all products under a particular category object
    context={'category':c,'product':p}
    return render(request,'products.html',context)

def product_details(request,p):
    p=Product.objects.get(id=p)
    context={'product':p}
    return render(request,'product_details.html',context)

def registration(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        f = request.POST['f']
        l = request.POST['l']
        e = request.POST['e']
        if (p == cp):
            u = User.objects.create_user(username=u, password=p, first_name=f, last_name=l, email=e)
            u.save()
            return redirect('shop:categories')
        else:
            return HttpResponse("Passwords are not same")
    return render(request,'registration.html')
def user_login(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            return redirect('shop:categories')
        else:
            return HttpResponse("Invalid Credentials")
    return render(request,'login.html')
@login_required
def user_logout(request):
    logout(request)
    return redirect('shop:user_login')



def add_categories(request):
    if(request.method=="POST"):
        n=request.POST['n']
        i=request.FILES['i']
        d=request.POST['d']

        c=Category.objects.create(name=n,image=i,description=d)
        c.save()
        return redirect('shop:categories')
    return render(request,'add_categories.html')


def add_product(request):
    if (request.method == "POST"):
        n = request.POST['n']
        i = request.FILES['i']
        d = request.POST['d']
        s = request.POST['s']
        p = request.POST['p']
        c = request.POST['c']


        category = Category.objects.get(name=c)
        p=Product.objects.create(name=n,image=i,desc=d,stock=s,price=p,category=category)
        p.save()
        return redirect('shop:categories')
    return render(request,'add_product.html')


def add_stock(request,i):
    product=Product.objects.get(id=i)
    if request.method=="POST":  #a/f form submssin
        product.stock=request.POST['n']
        product.save()
        return redirect('shop:product_details',i)
    context={'product':product}

    return render(request,'add_stock.html',context)