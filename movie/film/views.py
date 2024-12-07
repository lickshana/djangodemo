from django.shortcuts import render, redirect

from film.models import Movie

def home(request):
    m=Movie.objects.all()
    context={'movie':m}
    return render(request,'home.html',context)

def addmovie(request):
    if(request.method=="POST"):
        t=request.POST['t']
        d=request.POST['d']
        l=request.POST['l']
        y=request.POST['y']
        i=request.FILES['i']

        m=Movie.objects.create(title=t,description=d,language=l,year=y,image=i)
        m.save()
        return redirect('home')
    return  render(request,'addmovie.html')

def moviedetails(request,p):
    m = Movie.objects.get(id=p)
    context = {'movie': m}
    return  render(request,'moviedetails.html',context)

def delete(request,p):
    m= Movie.objects.get(id=p)
    m.delete()
    return redirect('home')

def edit(request,p):
    m=Movie.objects.get(id=p)  # read a particular record

    if(request.method=="POST"):
        m.title=request.POST['t']
        m.description=request.POST['d']
        m.language=request.POST['l']
        m.year=request.POST['y']
        if(request.FILES.get('i')==None):
            m.save()
        else:
            m.image=request.FILES.get('i')
        return redirect('home')

    context = {'movie':m}
    return render(request,'edit.html',context)