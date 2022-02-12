from django import forms
from .models import Business, Movie,Review
from django.forms import ImageField, ModelForm, TextInput, EmailInput, NumberInput,DateInput,Select

class MovieForm(forms.ModelForm):

    class Meta:
        model=Movie

        fields=['title','director','actor','poster','genre','release_date','comeout','content','running_time','url','video']
 
        widgets = {
            'title': TextInput(attrs={
                'class': "form-input",
                'style': 'max-width: 300px;',
                'placeholder': '영상의 타이틀을 적어주세요'
                
                }),
                'director': TextInput(attrs={
                'class': "form-input",
                'style': 'max-width: 300px;',
                'placeholder': '영상 감독의 이름을 적어주세요'
                
                }),
                'actor': TextInput(attrs={
                'class': "form-input",
                'style': 'max-width: 300px;',
                'placeholder': '영상의 주요 출연진들을 적어주세요'
                
                }),
                'genre': Select(attrs={
                'class': "form-input",
                'style': 'max-width: 300px;',
                'placeholder': '장르 선택'
                
                }),
                'release_date': DateInput(attrs={
                'class': "form-input",
                'style': 'max-width: 300px;',
                'placeholder': '영상의 개봉일을 적어주세요'
                
                }),
                'comeout': Select(attrs={
                'class': "form-input",
                'style': 'max-width: 300px;',
                'placeholder': '개봉 여부'
                
                }),
                'content': TextInput(attrs={
                'class': "form-contentinput",
                'style': 'max-width: 800px;',
                'placeholder': '''혹시나 소개를 작성하는데 막막하다면 다음 질문을 참고해보세요!
                🎤 이 영화는 어떤 영화이고, 어떠한 내용을 담고 있나요?🎤 이 영상을 제작하게 된 배경이 무엇인가요?🎤 이 영상이 가지고 있는 특별한 메시지가 있을까요?🎤 이 영상의 특별한 점이나 특징 같은게 있을까요?'
                '''
                }),
                'url': TextInput(attrs={
                'class': "form-input",
                'style': 'max-width: 500px;',
                'placeholder': '영상의 url을 적어주세요'
                }),
                'running_time': TextInput(attrs={
                'class': "form-input",
                'style': 'max-width: 500px;',
                'placeholder': '영상의 러닝타임을 적어주세요'
                }),
            
        }
class ReviewForm(forms.ModelForm):

    class Meta:
        model=Review 

        fields=('title','content','rating')
        widgets={
            'title': TextInput(attrs={
                'class': "form-input",
                'style': 'max-width: 300px;',
                'placeholder': '글의 제목을 적어주세요'
                
                }),
            
            
            'content': TextInput(attrs={
                'class': "form-contentinput",
                'style': 'max-width: 800px;',
                'placeholder': '''텍스트 에디터적용 예정'
                '''
                }),
            'rating': NumberInput(attrs={
                'class': "form-input",
                'style': 'max-width: 200px;',
                'placeholder': '영화 평점을 적어주세요 0~5'
                
                }),
                
        }

class BusinessForm(forms.ModelForm):

    class Meta:
        model=Business

        fields=('user','title','content','image')
        widgets={
            'title': TextInput(attrs={
                'class': "form-input",
                'style': 'max-width: 300px;',
                'placeholder': '글의 제목을 적어주세요'
                
                }),
            
            'content': TextInput(attrs={
                'class': "form-contentinput",
                'style': 'max-width: 800px;',
                'placeholder': '''텍스트 에디터적용 예정'
                '''
                }),

        }

from django import forms
from .models import *


class CommentPreviewForm(forms.ModelForm):

    class Meta:
        model = CommentPreview
        exclude = ('movie',)