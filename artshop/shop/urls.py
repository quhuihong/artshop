"""artshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from artshop.shop import views

urlpatterns = [
    url(r'^$', views.index, name='shop_index'),
    url(r'^user$', views.user_list, name='user_list'),
    url(r'^user/register$', views.user_register, name='user_register'),
    url(r'^user/login$', views.user_login, name='user_login'),
    url(r'^user/logout$', views.user_logout, name='user_logout'),
    url(r'^user/(?P<user_id>\d+)$', views.user_detail, name='user_detail'),
    url(r'^user/(?P<user_id>\d+)/update', views.user_update, name='user_update'),
    url(r'^user/(?P<user_id>\d+)/delete', views.user_delete, name='user_delete'),
    url(r'^api/user/list', views.api_user_list, name='api_user_list'),
]
