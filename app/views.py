import string
import random as rm

from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseRedirect

# homework 2
from django.urls import reverse
from django.views.generic import FormView

from app.forms import NameForm, MyLoginForm, SearchMassageForm, RegisterForm

# def chil(request):
#     return render(request, 'chil.html')
#
#
# def acricles(request):
#     return HttpResponse("Acricles static!!")
#
#
# # homework 2
# def base(request):
#     return render(request, 'base.html', {'rand_int': rm.randint(1, 100),
#                                          'rand_symbol': ''.join(rm.choice(string.ascii_lowercase)
#                                                                 for i in range(rm.randint(5, 10)))
#                                          })
#
#
# # homework 2
# def second(request):
#     return render(request, 'second.html')
#
#
# def archive(request):
#     return HttpResponse('Archive static')
#
#
# def users(request):
#     return HttpResponse('Users static')
#
#
# # homework 2
# def article_num(request, article_number=None, slug_text=''):
#     if slug_text:
#         return render(request, 'article_name.html')
#
#
# # homework 2
# def article_num_arch(request, archive, slug_text=''):
#     return render(request, "int.html", {'int': archive, 'text': slug_text})
#
#
# def users_dynamic(request, user_number):
#     return HttpResponse(
#         "This is a dynamic user #{}.".format(user_number))
#
#
# def ukr_phone_num(request, phone_num, phone_code):
#     return HttpResponse(f'Your phone number {phone_num} is correct!')
#
#
# def any_symbols(request, symbols):
#     return HttpResponse('Good!')
from app.models import CommentToArticle


@login_required(login_url='login/')
def index(request):
    return render(request, 'index.html')


def norm(request):
    return render(request, 'norm.html')


def ne_norm(request):
    return render(request, 'ne_norm.html')


def my_login(request):
    if request.method == 'POST':
        form = MyLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data.get('username'),
                                password=form.cleaned_data.get('password'))
            if user is not None:
                login(request, user)
                return render(request, 'index.html', {'form': user.username})
            form.add_error(None, 'We have no this user, please register first!')
        else:
            return HttpResponseRedirect('/ne_norm/')
    else:
        form = MyLoginForm()
    return render(request, 'login.html', {'forms': form})


def my_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


class MyFormView(FormView):
    template_name = 'index.html'
    http_method_names = ['get', 'post']
    form_class = NameForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return HttpResponseRedirect('/norm/')
        else:
            return HttpResponseRedirect('/ne_norm/')


def search_massage(request):
    if request.method == 'GET':
        form = SearchMassageForm(request.GET)
        if form.is_valid():
            user_request = form.cleaned_data.get('search')
            if user_request is not None:
                result = CommentToArticle.objects.filter(comment__icontains=user_request).values_list('comment',
                                                                                                      flat=True)
            else:
                result = CommentToArticle.objects.values('comment')
    return render(request, 'search_massage.html', {'form': form, 'result': result})


def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
        else:
            print(form.errors)
    else:
        form = RegisterForm()
    return render(request, 'registration.html', {'form': form})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'it`s ok')
            return redirect('change_password')
        else:
            messages.error(request, 'correct the error')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form, 'user': form.user.username})
