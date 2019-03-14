from django.shortcuts import render, redirect
from users.models import Groups

def welcome(request):
    if request.user.is_authenticated:
        return redirect('user_home')
    else:
        return render(request, 'chatbot/welcome.html')

