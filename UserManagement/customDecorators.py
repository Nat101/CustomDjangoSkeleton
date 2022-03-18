from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied


'''
Decorators for views that checks that the logged in user is a certain user type; redirects to the 403 page if not.
'''

#Active
def Active_required(function):
	def check_login(u):
		if not u.is_active:
			raise PermissionDenied('Authorized users only.')
		return True
	actual_decorator = user_passes_test(check_login)
	return actual_decorator(function)

#CategoryA
def CategoryA_required(function):
	def check_login(u):
		if not u.is_active:
			raise PermissionDenied('Authorized users only.')
		return True
	actual_decorator = user_passes_test(check_login)
	return actual_decorator(function)

#CategoryB
def CategoryB_required(function):
	def check_login(u):
		if not u.is_active:
			raise PermissionDenied('Authorized users only.')
		return True
	actual_decorator = user_passes_test(check_login)
	return actual_decorator(function)

#CategoryC
def CategoryC_required(function):
	def check_login(u):
		if not u.is_active:
			raise PermissionDenied('Authorized users only.')
		return True
	actual_decorator = user_passes_test(check_login)
	return actual_decorator(function)

