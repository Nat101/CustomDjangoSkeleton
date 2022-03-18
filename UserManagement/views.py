from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .customDecorators import Active_required


'''
This is the landing page after a user initially logs in.
'''
@login_required
@Active_required
def Home(request):
	context = {}
	return render(request, 'UserManagement/home.html', context)


'''
Custom Error Pages
'''	
def Error403(request, exception):
	context = {'exception': exception}
	return render(request, 'UserManagement/403.html', context)

def Error404(request, exception):
	return render(request, 'UserManagement/404.html', {})

def Error500(request):
	return render(request, 'UserManagement/500.html', {})
