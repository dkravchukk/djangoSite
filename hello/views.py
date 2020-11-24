from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
import json

def myView(request):
    return HttpResponseRedirect('/yourHello')

def yourView(request):
    return HttpResponse('Hello redirectWorld')

def sendFile(response):
   # img = open('apple-app-site-association', 'rb')
   # response = FileResponse(img)
   # return response
   with open('apple-app-site-association', 'r') as f:
       my_json_obj = json.load(f)
       return JsonResponse(my_json_obj)
