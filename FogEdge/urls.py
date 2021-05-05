"""FogEdge URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from oidc_provider import views
from django.contrib.auth import views as auth_views

from Fog.views import login_view, home_view, register_view
from ProxyIDP.views import my_view
from ForeignFog.views import oidc_login, foreignfog_home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name="login_view"),
    path('home', home_view, name="home_view"),
    path('register', register_view, name="register_view"),
    path('foreignfog', oidc_login, name="oidc_login"),
    path('foreignfog/home', foreignfog_home_view, name="foreignfog_home_view"),
    url(r'^openid/', include('oidc_provider.urls', namespace='oidc_provider')),
    url(r'^authorize/?$', views.AuthorizeView.as_view(), name='authorize'),
    url(r'^token/?$', csrf_exempt(views.TokenView.as_view()), name='token'),
    url(r'^userinfo/?$', csrf_exempt(views.userinfo), name='userinfo'),
    url(r'^end-session/?$', views.EndSessionView.as_view(), name='end-session'),
    url(r'^\.well-known/openid-configuration/?$', views.ProviderInfoView.as_view(),
        name='provider-info'),
    url(r'^introspect/?$', views.TokenIntrospectionView.as_view(), name='token-introspection'),
    url(r'^jwks/?$', views.JwksView.as_view(), name='jwks'),
    # url(r'^accounts/login/$', auth_views.LoginView, {'template_name': 'login.html'}, name='login'),
    url(r'^accounts/login/$', my_view, name='my_view'),
]
