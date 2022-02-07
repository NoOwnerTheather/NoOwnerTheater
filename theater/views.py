from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.db.models import Q

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

def business_search(request):
   if request.method == 'POST':
      searched = request.POST['searched']        
      if not searched:
         return redirect('theater:business_list')         
      businesses = Business.objects.filter(Q(title__contains=searched)|Q(content__contains=searched)).order_by('-id')
      ctx = {'searched': searched, 'businesses': businesses}
      return render(request, 'theater/business_search.html', context=ctx)

   else:
      return render(request, 'theater/business_search.html', {})