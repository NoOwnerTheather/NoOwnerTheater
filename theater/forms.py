from django import forms
from .models import *


class CommentPreviewForm(forms.ModelForm):

    class Meta:
        model = CommentPreview
        exclude = ('movie',)