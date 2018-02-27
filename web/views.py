# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import JsonResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from web.models import User, Token, Expense , Income
from datetime import datetime

@csrf_exempt

def submit_expense(request):
    """user submits an Expense"""
    if 'date' not in request.POST:
        date = datetime.now()
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token).get()

    Expense.objects.create(user= this_user, amount= request.POST['amount'],
    text = request.POST['text'], date = date
    )


    print ('Salam, Khosh Amadi')
    print request.POST
    return JsonResponse(
    {
    'status': 'ok',
    }, encoder=JSONEncoder)
# Create your views here.
