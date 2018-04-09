# encoding=utf-8
from hashlib import sha1

from django import forms
from django.shortcuts import render, redirect
from scrapy.http import response

from daydays.models import UserInfo


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
    print(r1)
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

            user = UserInfo()
            user.username = uname
            user.password = upwd3
            user.mail = uemail
            user.save()

            return redirect('/user/login/')

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
        if user[0].password == pwd2:
            request.session['username'] = request.POST['username']
            return redirect('/user/user_center_info/')
        else:
            return redirect('/user/login/')


def user_center_info(request):
    cname = request.session.get('username')
    name = UserInfo.objects.filter(username=cname)
    context = {'user': name}
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
