# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from forms import loginForm
from wistock.models import user, item

def home(request):
  return render_to_response('home.html')

@csrf_exempt
def login(request):
  if request.method == "POST":
    form = loginForm(request.POST)
    if form.is_valid():
      user_email = form.cleaned_data['email']
      logged_user = user.objects.get(email=user_email)
      request.session['logged_user_id'] = logged_user.id
    return HttpResponseRedirect('/main')
  else:
    form = loginForm()
    return render_to_response ('login.html', {'form': form})

def main(request):
  logged_user = get_logged_user_from_request(request)
  if logged_user:
    queryset = user.objects.all()
    table = simpleTable(queryset)
    return render_to_response ('main.html', {'logged_user': logged_user, 'table': table})
  else:
    return HttpResponseRedirect('/login')

def get_logged_user_from_request(request):
  if 'logged_user_id' in request.session:
    logged_user_id = request.session['logged_user_id']
    return user.objects.get(id=logged_user_id)
  else:
    return None
