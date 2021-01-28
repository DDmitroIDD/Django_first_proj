from django.contrib import admin
from django.urls import path, re_path

from app.views import index, norm, ne_norm, MyFormView, my_login, my_logout, search_massage, registration, \
    change_password

urlpatterns = [
    # path('', base, name='base'), # homework 2
    # path('second/', second, name='second'), # homework 2
    # path('second/chil/', chil, name='chil'), # homework 2
    # path('acrticles/archive/', archive, name='archive'),
    # path('users/', users, name='users'),
    # path('<int:article_number>/', article_num, name='article_number'), # homework 2
    # path('<int:article_number>/<slug:slug_text>/', article_num, name='article_name'), # homework 2
    # path('article/archive/<int:archive>/', article_num_arch, name='article_num_arch'), # homework 2
    # path('article/archive/<int:archive>/<slug:slug_text>/', article_num_arch, name='article_num_arch'), # homework 2
    # path('users/<int:user_number>/', users_dynamic, name='users'),
    # re_path(r'^((063|066|067|068|073|093|095|096|097|098|099)\d{7})/$', ukr_phone_num, name='correct_number'),
    # re_path(r'^([1-9a-f]{4}-[1-9a-f]{6})/$', any_symbols, name='symbols'),
    # path('', MyFormView.as_view(), name='index'),
    path('', index, name='index'),
    path('login/', my_login, name='login'),
    path('loginout/', my_logout, name='logout'),
    path('norm/', norm, name='norm'),
    path('ne_norm/', ne_norm, name='ne_norm'),
    path('search/', search_massage, name='search'),
    path('registration/', registration, name='registration'),
    path('password/', change_password, name='change_password')
]

