from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from UserManagement.customDecorators import Active_required, CategoryA_required, CategoryB_required, CategoryC_required



#This is the landing page after a user initially logs in.  The user must be logged in and be "active" to access this view
@login_required
@Active_required
def Home(request):
	context = {}
	return render(request, 'General/home.html', context)

@login_required
@Active_required
def GeneralAccess(request):
	pass


@login_required
@CategoryA_required
def RestrictedAccessA(request):
	pass

@login_required
@CategoryB_required
def RestrictedAccessB(request):
	pass

@login_required
@CategoryC_required
def RestrictedAccessC(request):
	pass
