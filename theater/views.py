from re import template
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import MovieForm
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


