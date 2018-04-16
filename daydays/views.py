# encoding=utf-8
import django_filters
from hashlib import sha1

from django.core.mail import send_mail
from django.http import HttpResponse
from .token_user import *
from article.models import ArticlesInfo
from django import forms
from django.shortcuts import render, redirect
from daydays.models import UserInfo
from .serializers import UserSerializers
from rest_framework import viewsets, filters


class FM(forms.Form):  # 建立一个验证类
    user_name = forms.CharField(max_length='20',
                                min_length='1',
                                error_messages={'required': '用户名不能为空'})  # 自定制的中文错误返回
    pwd = forms.CharField(
        max_length='40',
        min_length='6',
        error_messages={'required': '密码不能为空',
                        'max_length': '密码最大长度不能大于40',
                        'min_length': '密码最小长度不能小于20'}
    )
    email = forms.EmailField(error_messages={'required': '邮箱不能为空',
                                             'invalid': '邮箱格式错误'})


def register(request):
    return render(request, 'daydays/user/register.html')


def register_handle(request):
    obj = FM(request.POST)  # 生成一个表单验证类
    r1 = obj.is_valid()  # 验证输出的结果 成功为true  错误为false
    if r1:
        post = request.POST
        uname = post.get('user_name')
        upwd = post.get('pwd')
        upwd2 = post.get('cpwd')
        uemail = post.get('email')
        if upwd == upwd2:
            # 加密密码
            s1 = sha1()
            s1.update(upwd.encode('utf8'))
            upwd3 = s1.hexdigest()
            token = token_confirm.generate_validate_token(uname)

            user = UserInfo()
            user.username = uname
            user.password = upwd3
            user.token_read = token
            user.mail = uemail
            user.save()

            message = "\n".join(
                ['{0},欢迎注册易读'.format(uname), '请访问该链接，完成用户验证：', '/'.join([django_settings.DOMAIN, 'user', token])])
            send_mail('注册用户信息', message, '17770147931@163.com', [uemail], fail_silently=False)

            return HttpResponse("请登录到注册邮箱中验证用户，有效期为1个小时")

        else:
            return redirect('/user/register/')

    else:
        return redirect('/user/register/')


def login(request):
    return render(request, 'daydays/user/login.html')


def login_handle(request):
    post = request.POST
    username = post.get('username')
    pwd = post.get('pwd')
    s1 = sha1()
    s1.update(pwd.encode('utf8'))
    pwd2 = s1.hexdigest()
    user = UserInfo.objects.filter(username=username)
    if len(user) > 0:
        if user[0].token_read == "YD":
            if user[0].password == pwd2:
                request.session['username'] = request.POST['username']
                return redirect('/user/user_center_info/')
            else:
                return redirect('/user/login/')
        else:
            return HttpResponse("请验证邮箱后在登录哦！")


def user_center_info(request):
    cname = request.session.get('username')
    name = UserInfo.objects.filter(username=cname)
    aname_ids = request.session.get('aname_ids', 1)
    aname_list = []
    if aname_ids == '':
        aname_list.append(None)
    else:
        for aname_id in aname_ids:
            aname_list.append(ArticlesInfo.objects.get(id=int(aname_id)))
    context = {'user': name, 'aname_list': aname_list}
    return render(request, 'daydays/user/user_center_info.html', context)


def user_center_order(request):
    user = UserInfo.objects.all()
    context = {'user': user}
    return render(request, 'daydays/user/user_center_order.html', context)


def user_center_site(request):
    cname = request.session.get('username')
    user = UserInfo.objects.filter(username=cname)
    context = {'user': user}
    return render(request, 'daydays/user/user_center_site.html', context)


def user_center(request):
    user = UserInfo.objects.all()
    context = {'user': user}
    post = request.POST
    shou = post.get('shou')
    address = post.get('address')
    postcode = post.get('postcode')
    phonenumber = post.get('phonenumber')
    cname = request.session.get('username')
    users = UserInfo.objects.filter(username=cname)
    users.update(shou=shou,
                 address=address,
                 postcode=postcode,
                 phonenumber=phonenumber)
    return render(request, 'daydays/user/user_center.html', context)


def outlogin(request):
    request.session = None
    return render(request, 'daydays/user/outlogin.html')


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserSerializers


def active_user(request, token):
    try:
        username = token_confirm.confirm_validate_token(token)
    except:
        username = token_confirm.remove_validate_token(token)
        users = UserInfo.objects.filter(username=username)
        for user in users:
            user.delete()
        return HttpResponse('对不起，验证链接已经过期，请重新<a href="http://0.0.0.0:8000/user/register/"' + (
            django_settings.DOMAIN) + u'/login\">注册</a>')
    try:
        user = UserInfo.objects.get(username=username)
    except UserInfo.DoesNotExist:
        return HttpResponse("对不起，您所验证的用户不存在，请重新注册")
    user.state = True
    user.tokens = token
    user.token_read = 'YD'
    user.save()
    message = '验证成功，请进行<a href="http://0.0.0.0:8000/user/register/">登录</a>操作'
    return HttpResponse(message)
