from django.shortcuts import render, redirect, get_object_or_404
from .models import *

def main(request):
   return render(request, template_name='theater/main.html')