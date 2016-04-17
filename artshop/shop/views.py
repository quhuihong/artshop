# coding:utf-8

from django import forms
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from artshop.shop.models import ShopUser


# Create your views here.

def index(request):
    return HttpResponse(u"我的小店")


def user_detail(request, user_id):
    context = RequestContext(request, {
        'shop_user': ShopUser.objects.get(id=user_id),
    })

    return render_to_response('shop/user_detail.html', context)


# 定义表单模型
class UserForm(forms.Form):
    username = forms.CharField(label='用户名:', max_length=30)
    password = forms.CharField(label='密码:', widget=forms.PasswordInput())
    email = forms.EmailField(label='电子邮件:')


# Creat your view here

def user_register(request):
    context = RequestContext(request, {

    })
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            # 获取表单信息
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            email = uf.cleaned_data['email']
            # 将表单写入数据库
            user = ShopUser()
            user.username = username
            user.password = password
            user.email = email
            user.save()

            # 返回注册成功业
            return render_to_response('shop/user_register_success.html', {
                'shop_user': user,
            })
    else:
        uf = UserForm()
    context['uf'] = uf
    return render_to_response('shop/user_register.html', context)

@login_required
def user_update(request, user_id):
    shop_user = ShopUser.objects.get(id=user_id)
    context = RequestContext(request, {
        'shop_user': shop_user,
    })

    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            # 获取表单信息
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            email = uf.cleaned_data['email']
            # 将表单写入数据库
            shop_user.username = username
            shop_user.password = password
            shop_user.email = email
            shop_user.save()

            return redirect('user_detail', user_id=shop_user.id)
    else:
        uf = UserForm()
    context['uf'] = uf
    return render_to_response('shop/user_update.html', context)


def user_delete(request, user_id):
    context = RequestContext(request, {
        'user_id': user_id,
    })
    if request.method == 'POST':
        ShopUser.objects.get(id=user_id).delete()

        return redirect('user_list')
    else:
        return render_to_response('shop/user_delete.html', context)


def user_list(request):
    shop_user_list = ShopUser.objects.all()
    context = RequestContext(request, {
        'shop_user_list': shop_user_list,
    })

    return render_to_response('shop/user.html', context)

def user_login(request):
    context = RequestContext(request, {
    })
    user = auth.get_user(request)
    if user.is_authenticated():
        return redirect('user_list')

    if request.method == 'POST':
        # 获取表单用户密码
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        # 获取的表单数据与数据库进行比较
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            next_url = request.GET.get('next', None)
            if next_url is not None:
                return redirect(next_url)
            else:
                return render_to_response('shop/user_login_success.html', {'username': username})

    return render_to_response('shop/user_login.html', context)

def user_logout(request):
    auth.logout(request)
    return redirect('user_login')