from django.contrib import admin
from django.urls import path, re_path

from app.views import article_num, archive, users, article_num_arch, users_dynamic, ukr_phone_num, \
    any_symbols, second, base, chil

urlpatterns = [
    path('', base, name='base'), # homework 2
    path('second/', second, name='second'), # homework 2
    path('second/chil/', chil, name='chil'), # homework 2
    path('acrticles/archive/', archive, name='archive'),
    path('users/', users, name='users'),
    path('<int:article_number>/', article_num, name='article_number'), # homework 2
    path('<int:article_number>/<slug:slug_text>/', article_num, name='article_name'), # homework 2
    path('article/archive/<int:archive>/', article_num_arch, name='article_num_arch'), # homework 2
    path('article/archive/<int:archive>/<slug:slug_text>/', article_num_arch, name='article_num_arch'), # homework 2
    path('users/<int:user_number>/', users_dynamic, name='users'),
    re_path(r'^((063|066|067|068|073|093|095|096|097|098|099)\d{7})/$', ukr_phone_num, name='correct_number'),
    re_path(r'^([1-9a-f]{4}-[1-9a-f]{6})/$', any_symbols, name='symbols'),
]

