from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list':latest_question_list,
    }
    return HttpResponse(request, 'polls/index.html', context)

def detail(request, question_id):
    response = f"You are looking at question {question_id}"
    return HttpResponse(response)

def results(request, question_id):
    response = f"You are looking results of question {question_id}"
    return HttpResponse(response)

def vote(request, question_id):
    response = f"You are voting on question {question_id}"
    return HttpResponse(response)