from re import template
from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from .models import *

from django.db.models import Q
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

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
def movie_delete(request,pk):
   post=get_object_or_404(Movie,id=pk)
   post.delete()
   return redirect("theater:main")

   
def review_enroll(request,pk):
   
   if request.method=="POST":
      form=ReviewForm(request.POST)
      
      if form.is_valid():
         user=User.objects.get(username=request.user)
         movie=Movie.objects.get(id=pk)
         review=Review(
               title=form.cleaned_data['title'],
               content=form.cleaned_data['content'],
               rating=form.cleaned_data['rating'],
               user=user,
               movie=movie
            )
         review.save()
         return redirect('theater:main') 
         #임시용 코드

   else:
      form=ReviewForm()
      ctx={'form':form}
      return render(request,template_name='theater/review_enroll.html',context=ctx)

def review_fix(request,pk,gk):
   post=get_object_or_404(Review,id=gk)
   if request.method=="POST":
      form=ReviewForm(request.POST,instance=post)
        
      if form.is_valid():
         post=form.save()
         return redirect('theater:main')

   else:
      form=ReviewForm(instance=post)
      ctx={'form':form}
      return render(request,template_name='theater/review_enroll.html',context=ctx)
      # redirect랑 render 주소는 임시
def review_delete(request,pk,gk):
   post=get_object_or_404(Review,id=gk)
   post.delete()
   return redirect("theater:main")

def info_enroll(request):

    if request.method=="POST":
        form=InfoForm(request.POST,request.FILES)
        
        if form.is_valid():
            user=User.objects.get(username=request.user)
            
            business=Business(
               title=form.cleaned_data['title'],
               content=form.cleaned_data['content'],
               image=form.cleaned_data['image'],
               user=user,
            )
            business.save()
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
         return redirect('theater:business_list')

   else:
      form=InfoForm(instance=post)
      ctx={'form':form}
      return render(request,template_name='theater/info_enroll.html',context=ctx)
      # redirect랑 render 주소는 임시

def info_delete(request,pk):
   post=get_object_or_404(Business,id=pk)
   post.delete()
   return redirect("theater:main")


def preview(request):

    movie = Movie.objects.all()

    ctx = {'movie': movie}

    return render(request, template_name='theater/preview.html', context=ctx)


def preview_detail(request,pk):

    #movie=Movie.objects.get(id=pk)
    movie = get_object_or_404(Movie, pk=pk)
    #print(movie.comment_set.all())
    #preview_form = CommentPreviewForm()
    #preview_comments = movie.commentpreview_set.all()


    ctx = {
       'movie': movie,
       #'preview_form':preview_form,
       #'preview_comments':preview_comments,
       }

    return render(request, 'theater/preview_detail.html',context=ctx)


import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def like_ajax(request,pk):
    req=json.loads(request.body) # json 임퐅, {'id':1, 'type':'like'} 파이썬 딕셔너리 형태로 변환하여 req변수에 담아준다
    post_id=req['id']
    button_type=req['type']

    comment=CommentPreview.objects.get(id=post_id) #id가 1인 포스트를 찾아서 변수에 넣어준다

    if button_type=='like':
        comment.like+=1

    else:
        comment.like-=1


    comment.save()

    return JsonResponse({'id':post_id, 'type':button_type})



@csrf_exempt
def write_comment(request,pk):
   #print("hi")
   req = json.loads(request.body)
   id = req['id']
   type = req['type']
   content = req['content']
   user=req['user']

   movie = Movie.objects.get(id=id)
   comment = CommentPreview.objects.create(movie=movie, content=content, user=user)
   #print(comment)
   comment.save()
   return JsonResponse({'id': id, 'type': type, 'content': content, 'comment_id': comment.id})


@csrf_exempt
def del_comment(request,pk):
   req = json.loads(request.body)
   comment_id = req['id']
   comment = get_object_or_404(CommentPreview, id=comment_id)
   comment.delete()
   return JsonResponse({'id': comment_id})

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
   ctx = {'rows1':rows1, 'rows2':rows2, 'rows3':rows3,
   'current_user':request.user,
   'blame':'성인물(에로)'}

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
   ctx = {'movies' : movies,
   'current_user':request.user}

   return render(request, template_name='theater/movie_list_popular.html', context=ctx)

def movie_list_recent(request):
   movies = Movie.objects.filter(comeout='개봉').order_by('-release_date')
   ctx = {'movies' : movies,'current_user':request.user}

   return render(request, template_name='theater/movie_list_recent.html', context=ctx)

def genre_order(request):
   rows1 = Movie.objects.filter(comeout='개봉').order_by('-rating')[:20]
   rows3 = Movie.objects.filter(comeout='개봉').order_by('-release_date')[:20]

   sort = request.GET.get('so','')
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

   ctx = {'rows1':rows1, 'rows2':content_list, 'rows3':rows3, 'so':sort}

   return render(request, template_name='theater/chart_list.html', context=ctx) 
   
def movie_detail(request, pk):
   movie = Movie.objects.get(id=pk)
   reviews = movie.review_set.all()
   ctx = {
        'movie' : movie,
        'reviews' : reviews,
    }

   return render(request, template_name='theater/movie_detail.html', context=ctx)



   

@csrf_exempt
def business_hits_ajax(request):
   req = json.loads(request.body)
   business_id = req['id']
   business = Business.objects.get(id = business_id)
   business.hits += 1
   business.save()
   return 

