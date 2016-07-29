#-*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django import template
from django.contrib.sessions.models import Session
from django.contrib import auth
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def callback(request):
	return HttpResponse(request)
	#return render(request, 'callback.html', locals())
