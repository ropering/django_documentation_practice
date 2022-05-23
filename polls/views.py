from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import *


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse(f"Questions {question_id}")


def results(request, question_id):
    return HttpResponse(f"results of questions {question_id}")


def vote(request, question_id):
    return HttpResponse(f"voting in questions {question_id}")


