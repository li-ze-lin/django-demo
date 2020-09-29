from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# Create your views here.
def index(request):
    student_list = StudentMessage.objects.all()
    return render(request, 'student/index.html', {'student_list': student_list})

def to_add(request):
    return render(request, 'student/add.html')

def add(request):
    data = request.POST
    StudentMessage(name=data.get('name'), grade=data.get('grade')).save()
    student_list = StudentMessage.objects.all()
    return index(request)

def delete(request, student_id):
    StudentMessage.objects.filter(id=student_id).delete()
    return index(request)