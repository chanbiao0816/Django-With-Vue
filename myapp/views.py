import json
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.http import require_http_methods

from myapp.models import Book, Question, Option

# Create your views here.
@require_http_methods(["GET"])
def add_book(request):
    response = {}
    try:
        book = Book(book_name=request.GET.get('book_name'))
        book.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

@require_http_methods(["GET"])
def show_books(request):
    response = {}
    try:
        books = Book.objects.filter()
        response['list']  = json.loads(serializers.serialize("json", books))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

@require_http_methods(["GET"])
def add_answer(request):
    response = {}
    try:
        book = Book(book_name=request.GET.get('book_name'))
        book.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

@require_http_methods(["GET"])
def show_questions(request):
    response = {}
    try:
        questions = Question.objects.all()
        response['count'] = questions.count()
        response['data'] = []
        for question in questions:
            item = {'id': question.id, 'question_desc': question.question_desc, 'options': [], 'answer': ''}
            for option in question.option.all():
                item['options'].append({'id': option.id, 'option_desc': option.option_desc, 'option_value': option.option_value})
            response['data'].append(item)
        response['msg'] = 'success'
        response['code'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['code'] = 1

    return JsonResponse(response)


"""
context = {
    "data": [
        {
            "question_desc": "",
            "options": [
                {"option_desc": "", "option_value": ""}
            ]
        }
    ],
    "count":
    "msg": "",
    "code": 0
}
"""
