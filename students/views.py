from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def students(request):
    students = [
        {'id': 1, 'name': 'Durjoy', 'age': 22},
        {'id': 2, 'name': 'Ayesha', 'age': 21},
        {'id': 3, 'name': 'Rafi', 'age': 23},
    ]
    return HttpResponse(students)