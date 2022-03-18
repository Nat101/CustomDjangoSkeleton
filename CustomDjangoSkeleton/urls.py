from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import handler403, handler404, handler500
from django.contrib.auth import views as auth_views
 

urlpatterns = [
	path('admin/', admin.site.urls),
    
	#Login/ Logout #Note views are built into Django
	path('', auth_views.LoginView.as_view(template_name='UserManagement/login.html'), name='Login'),
	path('UserManagement/Logout', auth_views.LogoutView.as_view(), name='Logout'),

	#Password Reset (User not logged in) #Note views are built into Django
	re_path(r'^reset/$', auth_views.PasswordResetView.as_view( template_name='UserManagement/PasswordReset/passwordReset.html', email_template_name='UserManagement/PasswordReset/passwordResetEmail.html', subject_template_name='UserManagement/PasswordReset/passwordResetSubject.txt'), name='password_reset'),
	re_path(r'^reset/done/$', auth_views.PasswordResetDoneView.as_view(template_name='UserManagement/PasswordReset/passwordResetDone.html'), name='password_reset_done'),
	re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,32})/$', auth_views.PasswordResetConfirmView.as_view(template_name='UserManagement/PasswordReset/passwordResetConfirm.html'), name='password_reset_confirm'),
	re_path(r'^reset/complete/$', auth_views.PasswordResetCompleteView.as_view(template_name='UserManagement/PasswordReset/passwordResetComplete.html'), name='password_reset_complete'),

	#Password Change (User is logged in) #Note views are built into Django
	re_path(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='UserManagement/PasswordReset/passwordChange.html'), name='password_change'),
	re_path(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='UserManagement/PasswordReset/passwordChangeDone.html'), name='password_change_done'),
	
	#Apps
    path('General/', include('General.urls')),
	

]

#Error Pages
handler403 = 'UserManagement.views.Error403'
handler404 = 'UserManagement.views.Error404'
handler500 = 'UserManagement.views.Error500'