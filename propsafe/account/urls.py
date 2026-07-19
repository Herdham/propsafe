from . import views
from django.urls import path
from django.contrib.auth import views as auth_view

app_name = "account"

urlpatterns = [
    path('', views.home, name="home"),
    path('journal_option/', views.journal_option, name="journal"),
    path('account_setup/', views.mt5_account, name="account_setup"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('profile/<int:profile_id>/', views.profile, name="profile"),
    path('setting/<int:user_id>/', views.setting, name="setting"),
    path(
        'password_reset/', 
        auth_view.PasswordResetView.as_view(template_name="authentication/password_reset.html"), 
        name="password_reset"
    ),
    path(
        "password_reset_done/", 
        auth_view.PasswordResetDoneView.as_view(template_name="authentication/password_reset_done.html"), name="password_reset_done"
    ),
    path(
        "password_reset_confirm/<uidb64>/<token>/", 
         auth_view.PasswordResetConfirmView.as_view(template_name="authentication/password_reset_confirm.html"), 
         name="password_reset_confirm"
    ),
    path(
        "password_reset_complete/", 
         auth_view.PasswordResetCompleteView.as_view(template_name="authentication/password_reset_complete.html"), 
         name="password_reset_complete"
    )
]
