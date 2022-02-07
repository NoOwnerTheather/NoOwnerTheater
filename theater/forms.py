from django import forms
from .models import Business, Movie,Review


class MovieForm(forms.ModelForm):

    class Meta:
        model=Movie

        fields=('title','director','actor','poster','genre','release_date','comeout','content','running_time','url','video')


class ReviewForm(forms.ModelForm):

    class Meta:
        model=Review 

        fields=('title','content','rating')


class InfoForm(forms.ModelForm):

    class Meta:
        model=Business

        fields=('title','content','image')

