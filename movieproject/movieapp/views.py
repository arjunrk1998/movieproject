from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from movieapp.models import movie
from .forms import movieform

def fun(request):
    data=movie.objects.all()
    content={
        'movielist':data
    }
    return  render(request,'index.html',content)
def detail(request,movie_id):
    data=movie.objects.get(id=movie_id)
    return render(request,'detail.html',{'movie':data})
def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name',)
        dis=request.POST.get('dis',)
        year=request.POST.get('year',)
        img=request.FILES['img']
        data=movie(name=name,dis=dis,year=year,img=img)
        data.save()
    return render(request,'add.html')
def update(request,id):
    movies=movie.objects.get(id=id)
    form=movieform(request.POST or None,request.FILES,instance=movies)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movies})
def delete(request,id):
    if request.method=='POST':
        movies=movie.objects.get(id=id)
        movies.delete()
        return redirect('/')
    return render(request,'delete.html')



