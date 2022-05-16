"""djcrm_main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from leads import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import (
    LoginView,LogoutView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
    
    )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.LandingPageView.as_view() , name = 'home'),
    path('leads/',include('leads.urls')),
    path('agents/',include('agents.urls')),

    path('signup/', views.SignupView.as_view() , name = 'signup'),

    path('password_reset/', PasswordResetView.as_view(), name = 'password_reset'),
    path('password_reset_done/', PasswordResetDoneView.as_view(), name = 'password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name = 'password_reset_confirm'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(), name = 'password_reset_complete'),

    path('login/' , LoginView.as_view() , name = 'login'),
    path('loguot/' , LogoutView.as_view() , name = 'logout'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)