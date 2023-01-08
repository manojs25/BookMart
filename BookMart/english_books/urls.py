from django.contrib import admin
from django.urls import path
from english_books import views

app_name = 'english_books'

urlpatterns = [
    path('englishlist/', views.englishlist, name='englishlist'),
    path('potter2/', views.potter2, name='potter2'),
    path('potter7/', views.potter7, name='potter7'),
    path('potter3/', views.potter3, name='potter3'),
    path('wings/', views.wings, name='wings'),
    path('game1/', views.game1, name='game1'),
    path('harrypotter/', views.harrypotter, name='harrypotter'),
    path('rowling/',views.rowling, name='rowling')
]
