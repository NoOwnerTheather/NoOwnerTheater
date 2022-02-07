from re import template
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import MovieForm,ReviewForm,InfoForm
def main(request):
   return render(request, template_name='theater/main.html')




def movie_enroll(request):

    if request.method=="POST":
        form=MovieForm(request.POST,request.FILES)
        
        if form.is_valid():
            post=form.save()
            return redirect('theater:main')

    else:
        form=MovieForm()
        ctx={'form':form}
        return render(request,template_name='theater/enroll.html',context=ctx)


def movie_fix(request,pk):
   post=get_object_or_404(Movie,id=pk)
   if request.method=="POST":
      form=MovieForm(request.POST,request.FILES,instance=post)
        
      if form.is_valid():
         post=form.save()
         return redirect('theater:main',pk)

   else:
      form=MovieForm(instance=post)
      ctx={'form':form}
      return render(request,template_name='theater/enroll.html',context=ctx)
      # redirect랑 render 주소는 임시

def review_enroll(request):
   
   if request.method=="POST":
      form=ReviewForm(request.POST)
      
      if form.is_valid():
         post=form.save()
         return redirect('theater:main') 
         #임시용 코드

   else:
      form=ReviewForm()
      ctx={'form':form}
      return render(request,template_name='theater/review_enroll.html',context=ctx)

def review_fix(request,pk):
   post=get_object_or_404(Review,id=pk)
   if request.method=="POST":
      form=ReviewForm(request.POST,instance=post)
        
      if form.is_valid():
         post=form.save()
         return redirect('theater:main',pk)

   else:
      form=ReviewForm(instance=post)
      ctx={'form':form}
      return render(request,template_name='theater/review.html',context=ctx)
      # redirect랑 render 주소는 임시

def info_enroll(request):

    if request.method=="POST":
        form=InfoForm(request.POST,request.FILES)
        
        if form.is_valid():
            post=form.save()
            return redirect('theater:main')

    else:
        form=InfoForm()
        ctx={'form':form}
        return render(request,template_name='theater/info_enroll.html',context=ctx)


def info_fix(request,pk):
   post=get_object_or_404(Business,id=pk)
   if request.method=="POST":
      form=InfoForm(request.POST,request.FILES,instance=post)
        
      if form.is_valid():
         post=form.save()
         return redirect('theater:main',pk)

   else:
      form=InfoForm(instance=post)
      ctx={'form':form}
      return render(request,template_name='theater/info_enroll.html',context=ctx)
      # redirect랑 render 주소는 임시

