import string
import random as rm

from django.shortcuts import render

from django.http import HttpResponse


# homework 2
def chil(request):
    return render(request, 'chil.html')


def acricles(request):
    return HttpResponse("Acricles static!!")


# homework 2
def base(request):
    return render(request, 'base.html', {'rand_int': rm.randint(1, 100),
                                         'rand_symbol': ''.join(rm.choice(string.ascii_lowercase)
                                                                for i in range(rm.randint(5, 10)))
                                         })


# homework 2
def second(request):
    return render(request, 'second.html')


def archive(request):
    return HttpResponse('Archive static')


def users(request):
    return HttpResponse('Users static')


# homework 2
def article_num(request, article_number=None, slug_text=''):
    if slug_text:
        return render(request, 'article_name.html')
    else:
        return render(request, 'article_number.html')


# homework 2
def article_num_arch(request, archive, slug_text=''):
    return render(request, "int.html", {'int': archive, 'text': slug_text})


def users_dynamic(request, user_number):
    return HttpResponse(
        "This is a dynamic user #{}.".format(user_number))


def ukr_phone_num(request, phone_num, phone_code):
    return HttpResponse(f'Your phone number {phone_num} is correct!')


def any_symbols(request, symbols):
    return HttpResponse('Good!')
