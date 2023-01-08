from django.contrib import admin
from django.urls import path
from kannada_books import views

app_name = 'kannada_books'

urlpatterns = [
    path('kannadalist/', views.kannadalist, name='kannadalist'),
    path('jugaricross/', views.jugaricross, name='jugaricross'),
    path('marali/', views.marali, name='marali'),
    path('nenapu/', views.nenapu, name='nenapu'),
    path('kanooru/', views.kanooru, name='kanooru'),
    path('karvalo/', views.karvalo, name='karvalo'),
    path('mookajji/', views.mookajji, name='mookajji'),
    path('magalu/', views.magalu, name='magalu'),
    path('millenium', views.millenium, name='millenium'),
    path('tejaswi', views.tejaswi, name='tejaswi'),
    path('karantha', views.karantha, name='karantha'),
]
