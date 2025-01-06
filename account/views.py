from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
users = ['amir', 'reza', 'sara', 'taraneh']
blocked_user = ['amir']

def profile(request, username):
    if(username == 'reza'):
         return render(request, 'account/index.html', {'username' : 'رضا مردانی'})
   