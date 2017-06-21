from django.shortcuts import render, get_object_or_404
from digiTech.forms import *
from django.contrib.auth.tokens import default_token_generator
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.contrib.auth import login, authenticate, logout
from django.db import transaction
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required


def home(request):
    context = {}
    context['user'] = request.user
    return render(request, 'digiTech/home.html', context)


def handler_404(request):
    return render(request, 'digiTech/404.html')


@transaction.atomic()
def registration(request):
    logout(request)
    if request.method == 'GET':
        return render(request, 'digiTech/registration.html', {'form': RegistrationForm()})
    regist_form = RegistrationForm(request.POST)
    context = {}
    context['form'] = regist_form
    if not regist_form.is_valid():
        context['has_error'] = True
        return render(request, 'digiTech/registration.html', context)
    new_user = User.objects.create_user(username=regist_form.cleaned_data['username'],
                                        password=regist_form.cleaned_data['password2'],
                                        email=regist_form.cleaned_data['email'])
    new_user.is_active = False
    new_user.save()
    new_person = Person(user=new_user, school=regist_form.cleaned_data['school'],
                        location=regist_form.cleaned_data['location'])
    new_person.save()
    context['information'] = '您已注册成功，请点击邮箱中的链接激活账户'
    context['has_error'] = False
    token = default_token_generator.make_token(new_user)
    email_body = """
欢迎成为KY Coding注册用户，请点击链接激活账号：
  http://%s%s
""" % (request.get_host(),
       reverse('account_activate', args=(new_user.username, token)))
    send_mail(subject="账号激活 | KY Coding",
              message=email_body,
              from_email="liangxt07@gmail.com",
              recipient_list=[new_user.email])
    return render(request, 'digiTech/registration.html', context)


@transaction.atomic()
def user_authenticate(request):
    if request.method == 'GET':
        return render(request, 'digiTech/login.html', {'form': LoginForm()})
    login_form = LoginForm(request.POST)
    if not login_form.is_valid():
        return render(request, 'digiTech/login.html', {'form': login_form})
    username = login_form.cleaned_data['username']
    password = login_form.cleaned_data['password']
    context = {}
    context['form'] = login_form
    context['has_error'] = True
    if not User.objects.filter(username__exact=username):
        context['information'] = '用户不存在'
        return render(request, 'digiTech/login.html', context)
    user = authenticate(username=username, password=password)
    if user is None:
        context['information'] = '密码错误或账号未激活'
        return render(request, 'digiTech/login.html', context)
    login(request, user)
    return HttpResponseRedirect('/digiTech/')


@transaction.atomic()
def password_reset(request, username, token):
    logout(request)
    user = get_object_or_404(User, username=username)
    if not default_token_generator.check_token(user, token):
        raise Http404
    context = {}
    context['username'] = username
    context['token'] = token
    if request.method == 'GET':
        context['form'] = PasswordResetForm()
        return render(request, 'digiTech/password_reset.html', context)
    password_reset_form = PasswordResetForm(request.POST)

    context['form'] = password_reset_form
    if not password_reset_form.is_valid():
        context['form_error'] = '两次密码输入不一致'
        return render(request, 'digiTech/password_reset.html', context)
    user.set_password(password_reset_form.cleaned_data['password2'])
    user.save()
    context['information'] = True
    login(request, user)
    return render(request, 'digiTech/password_reset.html', context)


@transaction.atomic()
def password_forget(request):
    if request.method == 'GET':
        return render(request, 'digiTech/password_forget.html', {'form': PasswordForgetForm()})
    password_forget_form = PasswordForgetForm(request.POST)
    if not password_forget_form.is_valid():
        return render(request, 'digiTech/password_forget.html', {'form': password_forget_form})
    nameoremail = password_forget_form.cleaned_data['nameoremail']
    user1 = User.objects.filter(email__exact=nameoremail)
    user2 = User.objects.filter(username__exact=nameoremail)
    context = {}
    context['form'] = password_forget_form
    if not user1 and not user2:
        context['form_error'] = '用户名或邮箱不存在'
        return render(request, 'digiTech/password_forget.html', context)
    if user1 and not User.objects.get(email=nameoremail).is_active:
        context['form_error'] = '账户未被激活'
        return render(request, 'digiTech/password_forget.html', context)
    if user2 and not User.objects.get(username=nameoremail).is_active:
        context['form_error'] = '账户未被激活'
        return render(request, 'digiTech/password_forget.html', context)
    if user1:
        user = User.objects.get(email=nameoremail)
        password_forget_helper(request, user)
    else:
        user = User.objects.get(username=nameoremail)
        password_forget_helper(request, user)
    context['information'] = '请点击注册邮箱中的链接修改密码'
    return render(request, 'digiTech/password_forget.html', context)


def password_forget_helper(request, user):
    token = default_token_generator.make_token(user)
    email_body = """
            您好！请点击链接重设密码:
              http://%s%s
            """ % (request.get_host(),
                   reverse('password_reset', args=(user.username, token)))
    send_mail(subject="密码修改 | KY Coding",
              message=email_body,
              from_email="liangxt07@gmail.com",
              recipient_list=[user.email])


@transaction.atomic()
def account_activate(request, username, token):
    logout(request)
    user = get_object_or_404(User, username=username)
    if not default_token_generator.check_token(user, token):
        raise Http404
    user.is_active = True
    user.save()
    return render(request, 'digiTech/account_activate.html')


@login_required()
def profile_edit(request):
    return render(request, 'digiTech/profile_edit.html')


@login_required()
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/digiTech/')

