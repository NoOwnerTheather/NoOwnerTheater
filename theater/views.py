from multiprocessing import context
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

def chart_list(request):
   rows1 = Movie.objects.filter(comeout='개봉').order_by('-rating')[:20]
   rows2 = Movie.objects.filter(comeout='개봉').order_by('?')[:20]
   rows3 = Movie.objects.filter(comeout='개봉').order_by('-release_date')[:20]
   ctx = {'rows1':rows1, 'rows2':rows2, 'rows3':rows3}

   return render(request, template_name='theater/chart_list.html', context=ctx) 

def movie_search(request):
   if request.method == 'POST':
      searched = request.POST['searched']        
      if not searched:
         return redirect('theater:chart_list')         
      movies = Movie.objects.filter(title__contains=searched)
      ctx = {'searched': searched, 'movies': movies}

      return render(request, 'theater/movie_searched.html', context=ctx)
   else:
      return render(request, 'theater/movie_searched.html', {})

def movie_list_popular(request):
   movies = Movie.objects.filter(comeout='개봉').order_by('-rating')
   ctx = {'movies' : movies}

   return render(request, template_name='theater/movie_list_popular.html', context=ctx)

def movie_list_recent(request):
   movies = Movie.objects.filter(comeout='개봉').order_by('-release_date')
   ctx = {'movies' : movies}

   return render(request, template_name='theater/movie_list_recent.html', context=ctx)

def genre_order(request):
   rows1 = Movie.objects.filter(comeout='개봉').order_by('-rating')[:20]
   rows3 = Movie.objects.filter(comeout='개봉').order_by('-release_date')[:20]

   sort = request.GET.get('sort','')
   if sort == '1':
      content_list = Movie.objects.filter(comeout='개봉', genre='드라마').order_by('-id')[:20]
   elif sort ==  '2':
      content_list = Movie.objects.filter(comeout='개봉', genre='멜로/로맨스').order_by('-id')[:20]
   elif sort ==  '3':
      content_list = Movie.objects.filter(comeout='개봉', genre='다큐멘터리').order_by('-id')[:20]
   elif sort ==  '4':
      content_list = Movie.objects.filter(comeout='개봉', genre='코미디').order_by('-id')[:20]
   elif sort ==  '5':
      content_list = Movie.objects.filter(comeout='개봉', genre='액션').order_by('-id')[:20]
   elif sort ==  '6':
      content_list = Movie.objects.filter(comeout='개봉', genre='가족').order_by('-id')[:20]
   elif sort ==  '7':
      content_list = Movie.objects.filter(comeout='개봉', genre='미스터리').order_by('-id')[:20]
   elif sort ==  '8':
      content_list = Movie.objects.filter(comeout='개봉', genre='스릴러').order_by('-id')[:20]
   elif sort ==  '9':
      content_list = Movie.objects.filter(comeout='개봉', genre='범죄').order_by('-id')[:20]
   elif sort ==  '10':
      content_list = Movie.objects.filter(comeout='개봉', genre='공포(호러)').order_by('-id')[:20]
   elif sort ==  '11':
      content_list = Movie.objects.filter(comeout='개봉', genre='SF').order_by('-id')[:20]
   elif sort ==  '12':
      content_list = Movie.objects.filter(comeout='개봉', genre='판타지').order_by('-id')[:20]
   elif sort ==  '13':
      content_list = Movie.objects.filter(comeout='개봉', genre='성인물(에로)').order_by('-id')[:20]
   elif sort ==  '14':
      content_list = Movie.objects.filter(comeout='개봉', genre='전쟁').order_by('-id')[:20]
   elif sort ==  '15':
      content_list = Movie.objects.filter(comeout='개봉', genre='애니메이션').order_by('-id')[:20]
   elif sort ==  '16':
      content_list = Movie.objects.filter(comeout='개봉', genre='사극').order_by('-id')[:20]
   elif sort ==  '17':
      content_list = Movie.objects.filter(comeout='개봉', genre='뮤지컬').order_by('-id')[:20]
   else:
      content_list = Movie.objects.filter(comeout='개봉').order_by('?')[:20]



   ctx = {'rows1':rows1, 'rows2':content_list, 'rows3':rows3}

   return render(request, template_name='theater/chart_list.html', context=ctx) 
   



   