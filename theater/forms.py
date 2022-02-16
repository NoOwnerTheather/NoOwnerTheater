from django import forms
from .models import Business, Movie,Review
from django.forms import ImageField, ModelForm, TextInput, EmailInput, NumberInput,DateInput,Select
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django_summernote.widgets import SummernoteWidget
class MovieForm(forms.ModelForm):
    content: forms.CharField(widget=CKEditorUploadingWidget())
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
                'placeholder': '개봉일을 2022-01-01 형식으로 적어주세요!'
                
                }),
                'comeout': Select(attrs={
                'class': "form-input",
                'style': 'max-width: 300px;',
                'placeholder': '개봉 여부'
                
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
             'content': SummernoteWidget(attrs={'summernote': {'width': '800px', 'height': '380px'}}),
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
            # 'rating': NumberInput(attrs={
            #     'class': "form-input",
            #     'style': 'max-width: 300px;',
            #     'placeholder': '영화 평점을 적어주세요 0~5'
                
            #     }),
                
        }

class BusinessForm(forms.ModelForm):

    class Meta:
        model=Business

        fields=('title','content','image')
        widgets={
            'title': TextInput(attrs={
                'class': "form-input",
                'style': 'max-width: 300rem;border:',
                'placeholder': '  글의 제목을 적어주세요'
                
                }),
            
            
            'content': SummernoteWidget(attrs={'summernote': {
                'width': '800px', 
                'height': '380px',
                'placeholder':'''게시물에 들어가야할 항목들은 아래와 같습니다!<br><br><br>


🎤 정확한 날짜
<br><br>

🎤 연락처
<br><br>

🎤 지원사업 혹은 행사에 대한 정보
<br><br>
'''

                }}),


        }
        
        def clean(self):
            cleaned_data=super().clean()

            title=cleaned_data.get('title','')
            content=cleaned_data.get('contents','')
            if title=='':
                self.add_error('title','글 제목을 입력하세요')
            elif content=='':
                self.add_error('contents','글 내용을 입력하세요!')
            else:
                self.title=title
                self.content=content

from django import forms
from .models import *


class CommentPreviewForm(forms.ModelForm):

    class Meta:
        model = CommentPreview
        exclude = ('movie',)