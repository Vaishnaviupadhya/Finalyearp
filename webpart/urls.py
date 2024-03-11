"""
URL configuration for webpart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from home.views import *
from django.contrib.auth import views  as auth_views
from .forms import CustomPasswordResetForm
from django.urls import reverse_lazy
urlpatterns = [
    path('', home ,name="home"),
    path('braind/', braind ,name="braind"),
    path('logins/', logins ,name="logins"),
    path('signup/', signup ,name="signup"),
    path('logins/homep/',homep,name="homep"),
    path('logins/homed/',homed,name="homed"),
    path('logoutp/', logoutp, name="logoutp"),
    path('admin/', admin.site.urls),
    # path('reset_password/',auth_views.PasswordResetView.as_view(),name="reset_password"),
    # path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    # path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    # path('reset_password_complete',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_complete"),
    path('password_reset/', auth_views.PasswordResetView.as_view(
        form_class=CustomPasswordResetForm,
        email_template_name='registration/password_reset_email.html',
        success_url=reverse_lazy('password_reset_done'),
    ), name="password_reset"),

    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('password_reset_complete')), name="password_reset_confirm"),
     path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(success_url='/logins/',  
    ), name="password_reset_confirm"),

    
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

]
