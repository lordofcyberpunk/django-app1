from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'apptwo'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('settings/',views.UpdateAccountSetting.as_view(),name='edit_account'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('change-password/', auth_views.PasswordChangeView.as_view(
        template_name='change-password.html', success_url='/'), name='change-password'),
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='password_reset.html',
        subject_template_name='password_reset_subject.txt',
        email_template_name='password_reset_email.html'
    )
         , name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_complete.html'), name='password_reset_complete'),
]
