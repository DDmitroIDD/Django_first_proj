from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def acricles(request):
    return HttpResponse("Acricles static!!")


def index(request):
    return HttpResponse("Static!!")


def archive(request):
    return HttpResponse('Archive static')


def users(request):
    return HttpResponse('Users static')


def article_num(request, article_number, slug_text=''):
    return HttpResponse(
        "This is a dynamic article number {}. {}".format(article_number, "slug text dynamic is {}".format(
            slug_text) if slug_text else "This is slug text"))


def article_num_arch(request, archive):
    return HttpResponse(
        "This is a dynamic archive #{}. {}".format(archive, "This is unnamed archive"))


def users_dynamic(request, user_number):
    return HttpResponse(
        "This is a dynamic user #{}.".format(user_number))


def ukr_phone_num(request, phone_num,  phone_code):
    return HttpResponse(f'Your phone number {phone_num} is correct!')


def any_symbols(request, symbols):
    return HttpResponse('Good!')
