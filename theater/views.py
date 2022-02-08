from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *


def main(request):
   return render(request, template_name='theater/main.html')




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
