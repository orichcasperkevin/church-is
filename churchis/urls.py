"""churchis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views

from rest_framework_simplejwt import views as jwt_views
from Clients import views as site_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),

    path('', site_views.index,name='home'),
    path('anvilAdmin/' ,site_views.anvil_admin, name="anvilAdmin"),

    path('get-anvil/',site_views.get_anvil,name='get_anvil'),
    path('add-credit/<slug:client_id>/',site_views.add_credit, name='add_credit'),
    path('edit-sms-credentials/<int:client_id>/',site_views.edit_SMS_credentials,name='edit_SMS_credentials'),
    path('try-demo/',site_views.get_demo,name='try_demo'),
    path('change-password/<slug:username>/<slug:church_name>/',site_views.change_password, name='change_password'),
    path('password-fail', site_views.password_fail),

    #django rich RichTextField
    path('djrichtextfield/', include('djrichtextfield.urls')),
    # jwt authentication
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    # apps
    path('api/clients/', include('Clients.api.urls')),
    path('api/members/', include('member.api.urls')),
    path('api/groups/', include('groups.api.urls')),
    path('api/events/', include('events.api.urls')),
    path('api/projects/', include('projects.api.urls')),
    path('api/finance/', include('finance.api.urls')),
    # path('api/news/', include('news.api.urls')),
    path('api/sermons/', include('sermons.api.urls')),
    path('api/services/', include('services.api.urls')),
    path('api/sms/', include('sms.api.urls')),
    path('api/social/', include('church_social.api.urls')),
]
