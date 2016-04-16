# coding:utf-8

from django.shortcuts import render
from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.template import RequestContext
from shop.models import User


# Create your views here.

def index(request):
    return HttpResponse(u"我的小店")


# 定义表单模型
# class UserForm(forms.Form):
#     username = forms.CharField(label='用户名:', max_length=30)
#     password = forms.CharField(label='密码:', widget=forms.PasswordInput())
#     email = forms.EmailField(label='电子邮件:')


# Creat your view here

# def register(request):
#     if request.method == 'POST':
#         uf = UserForm(request.POST)
#         if uf.is_valid():
#             # 获取表单信息
#             username = uf.cleaned_data['username']
#             password = uf.cleaned_data['password']
#             email = uf.cleaned_data['email']
#             # 将表单写入数据库
#             user = User()
#             user.username = username
#             user.password = password
#             user.email = email
#             user.save()
#             #返回注册成功业
#             return render_to_response('success.html',{'username':username})
#         else:
#             uf = UserForm()
#         return render_to_response('riegister.html',{'uf':uf})
