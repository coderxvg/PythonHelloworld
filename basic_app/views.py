from django.shortcuts import render
import pyodbc
from .models import Question
from django.utils import timezone
# Create your views here.
def index(request):
    q = Question.objects.all()
    return render(request,'index.html',{'q':q})



                