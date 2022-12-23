from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    if request.method == 'GET':     
        print()
        var = ''
        if var is not None:
            return render(request, 'menu2.html')
        else: 
            return redirect('loginIndex')