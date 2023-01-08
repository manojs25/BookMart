from django.shortcuts import render
from kannada_books import forms
from home.models import User
# Create your views here.


def kannadalist(request):
    return render(request, 'kannada_books/kannadalist.html')

def tejaswi(request):
    return render(request, 'kannada_books/tejaswi.html')

def karantha(request):
    return render(request, 'kannada_books/karantha.html')

def jugaricross(request):
    values = {'title':'Jugari Cross','book_name':'Jugari Cross','author':'K.P.Poornachandra Tejaswi','price':200,'rating':'4.8','Language':'Kannada','Publisher':'Pusthaka Prakashana','Binding':'Hardcore','image':'images/p5.jpeg'}
    return render(request, 'kannada_books/kannadabook_template.html', values)

def marali(request):
    values = {'title':'Marali Mannige','book_name':'Marali Mannige','author':'Shivarama Karantha','price':350,'rating':'4.7','Language':'Kannada','Publisher':'Sapna Book House','Binding':'Hardcore','image':'images/s4.jpg'}
    return render(request, 'kannada_books/kannadabook_template.html', values)

def nenapu(request):
    values = {'title':'Annana Nenapu','book_name':'Annana Nenapu','author':'K.P.Poornachandra Tejaswi','price':225,'rating':'4.5','Language':'Kannada','Publisher':'Sapna Book House','Binding':'Hardcore','image':'images/p3.jpg'}
    return render(request, 'kannada_books/kannadabook_template.html', values)

def kanooru(request):
    values = {'title':'Kanooru Heggadati','book_name':'Kanooru Heggadati','author':'Kuvempu','price':560,'rating':'4.6','Language':'Kannada','Publisher':'Udayaravi Prakashana','Binding':'Hardcore','image':'images/k1.jpg'}
    return render(request, 'kannada_books/kannadabook_template.html', values)

def karvalo(request):
    values = {'title':'Karvalo','book_name':'Karvalo','author':'K.P.Poornachandra Tejaswi','price':105,'rating':'4.4','Language':'Kannada','Publisher':'Pusthaka Prakashana','Binding':'Hardcore','image':'images/p6.jpeg'}
    return render(request, 'kannada_books/kannadabook_template.html', values)

def mookajji(request):
    values = {'title':'Mookajjiya Kanasugalu','book_name':'Mookajjiya Kanasugalu','author':'Shivarama Karantha','price':175,'rating':'4.8','Language':'Kannada','Publisher':'Sapna Book House','Binding':'Paperback','image':'images/s1.jpg'}
    return render(request, 'kannada_books/kannadabook_template.html', values)

def magalu(request):
    values = {'title':'Malegalalli Madumagalu','book_name':'Malegalalli Madumagalu','author':'Kuvempu','price':350,'rating':'4.7','Language':'Kannada','Publisher':'Sapna Book House','Binding':'Hardcore','image':'images/k2.jpg'}
    return render(request, 'kannada_books/kannadabook_template.html', values)

def millenium(request):
    values = {'title':'Millenium Series','book_name':'Millenium Series','author':'K.P.Poornachandra Tejaswi','price':1590,'rating':'4.8','Language':'Kannada','Publisher':'Pusthaka Prakashana','Binding':'Paperback','image':'images/p1.jpg'}
    return render(request, 'kannada_books/kannadabook_template.html', values)
