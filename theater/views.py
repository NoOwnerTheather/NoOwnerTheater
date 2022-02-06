from django.shortcuts import render, redirect, get_object_or_404
from .models import *

def main(request):
   return render(request, template_name='theater/main.html')

def business_list(request):
   businesses = Business.objects.all().order_by('-id')
   ctx = {'businesses' : businesses}

   return render(request, template_name='theater/business_list.html', context=ctx)

def business_detail(request, pk):
   business = Business.objects.get(id=pk)
   ctx = {'business' : business}

   return render(request, template_name='theater/business_detail.html', context=ctx) 

def chart_list(request):
   rows1 = Movie.objects.filter(comeout='개봉').order_by('-rating')[:20]
   rows2 = Movie.objects.filter(comeout='개봉', genre='드라마').order_by('-id')[:20]
   rows3 = Movie.objects.filter(comeout='개봉').order_by('-release_date')[:20]
   ctx = {'rows1':rows1, 'rows2':rows2, 'rows3':rows3}

   return render(request, template_name='theater/chart_list.html', context=ctx) 

   