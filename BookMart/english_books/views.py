from django.shortcuts import render

# Create your views here.

def englishlist(request):
    return render(request,'english_books/englishlist.html')

def rowling(request):
    return render(request,'english_books/rowling.html')

def potter2(request):
    values = {'title':'HARRY POTTER and the Chamber of Secrets','book_name':'HARRY POTTER and the Chamber of Secrets','author':'J.K.Rowling','price':265,'rating':'4.6','Language':'English','Publisher':'Bloomsbury Publishing','Binding':'Paperback','image':'images/h4.jpg'}
    return render(request, 'english_books/englishbook_template.html', values)

def potter3(request):
    values = {'title':'HARRY POTTER and the Prioner of Azkaban','book_name':'HARRY POTTER and the Prioner of Azkaban','author':'J.K.Rowling','price':415,'rating':'4.5','Language':'English','Publisher':'Bloomsbury Publishing','Binding':'Paperback','image':'images/h5.jpg'}
    return render(request, 'english_books/englishbook_template.html', values)

def potter7(request):
    values = {'title':'HARRY POTTER and the Deathly Hallows','book_name':'HARRY POTTER and the Deathly Hallows','author':'J.K.Rowling','price':440,'rating':'4.8','Language':'English','Publisher':'Bloomsbury Publishing','Binding':'Paperback','image':'images/h6.jpg'}
    return render(request, 'english_books/englishbook_template.html', values)

def wings(request):
    values = {'title':'Wings of Fire','book_name':'Wings of Fire','author':'A.P.J.Abdul Kalam and Tiwari Arun','price':260,'rating':'4.6','Language':'English','Publisher':'Bloomsbury Publishing','Binding':'Paperback','image':'images/e5.jpg'}
    return render(request, 'english_books/englishbook_template.html', values)

def game1(request):
    values = {'title':'A Game of Thrones','book_name':'A Game of Thrones','author':'George R.R Martin','price':440,'rating':'4.7','Language':'English','Publisher':'Bloomsbury Publishing','Binding':'Paperback','image':'images/e2.jpg'}
    return render(request, 'english_books/englishbook_template.html', values)

def harrypotter(request):
    values = {'title':'Harry Potter','book_name':'Harry Potter','author':'J.K.Rowling','price':3520,'rating':'4.7','Language':'English','Publisher':'Bloomsbury Publishing','Binding':'Paperback','image':'images/h1.jpg'}
    return render(request, 'english_books/englishbook_template.html', values)
