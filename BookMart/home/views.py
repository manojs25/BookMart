from django.http import HttpResponse
from django.shortcuts import render
from home import forms
from home.models import User
from home.models import Order
# Create your views here.

def home(request):
    if request.session.has_key('mobile'):
        return render(request,'home/home.html')
    else:
        return login(request)

def millenium(request):
    if request.session.has_key('mobile'):
        return render(request, 'home/millenium.html')
    else:
        return login(request)

def langoption(request):
    if request.session.has_key('mobile'):
        return render(request,'home/langoption.html')
    else:
        return login(request)

def loginconf(request,n):
    if request.session.has_key('mobile'):
        return render(request, 'home/loginconf.html', {'name':n})
    else:
        return login(request)

def update_confirm(request):
    if request.session.has_key('mobile'):
        return render(request, 'home/update_confirm.html')
    else:
        return login(request)


def authors(request):
    if request.session.has_key('mobile'):
        return render(request, 'home/authors.html')
    else:
        return login(request)



def register(request):
    form = forms.UserForm()

    if (request.method == 'POST'):
        form = forms.UserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return home(request)
        else:
            print("Error")
    return render(request, 'home/register.html',{'form':form})

def login(request):
    form = forms.LoginForm()

    if(request.method == 'POST'):
        form = forms.LoginForm(request.POST)

        if form.is_valid():
            mob = form.cleaned_data['mobile']
            u = User.objects.filter(mobile=mob)
            if u:
                for rec in u:
                    n = rec.name
                    m = rec.mobile
                    request.session['mobile'] = m
            return loginconf(request,n)
    return render(request, 'home/login.html',{'form':form})

def logincheck(request):
    if request.session.has_key('mobile'):
        n = request.session['mobile']
        print(n)
        return loginconf(request,n)
    else:
        return login(request)

def logout(request):
    del request.session['mobile']
    #return HttpResponse("<strong>You are logged out</strong>")
    return render(request,'home/logoutconf.html')

def profile(request):
    if request.session.has_key('mobile'):
        user_profile={}
        user = User.objects.filter(mobile=request.session['mobile'])
        if user:
            for a in user:
                user_profile['name'] = a.name
                user_profile['mobile'] = a.mobile
                user_profile['email'] = a.email
                user_profile['dob'] = a.dob
                user_profile['address'] = a.address
        return render(request, 'home/profile.html', {'user_profile':user_profile})
    else:
        return login(request)

def profile_update(request):
    if request.session.has_key('mobile'):
        form = forms.ProfileForm()

        if (request.method == 'POST'):
            form = forms.ProfileForm(request.POST)

            if form.is_valid():
                user = User.objects.filter(mobile=request.session['mobile']).update(name = form.cleaned_data['name'], email = form.cleaned_data['email'], address = form.cleaned_data['address'])
                return update_confirm(request)
            else:
                print("Error")
        return render(request, 'home/profile_update.html',{'form':form})
    else:
        return login(request)

def order(request,book,author,price):
    if request.session.has_key('mobile'):
        print(book)
        print(author)
        print(price)
        user = User.objects.filter(mobile=request.session['mobile'])
        for a in user:
            name = a.name
            mobile = a.mobile
        order = Order.objects.create(uname=name, mobile=mobile, book_name=book, author=author, price=price)
        return render(request, 'home/order_confirmation.html',{'book':book,'author':author,'price':price})
    else:
        return login(request)


def order_details(request):
    if request.session.has_key('mobile'):
        form = forms.OrderDeleteForm()

        if (request.method == 'POST'):
            form = forms.OrderDeleteForm(request.POST)

            if form.is_valid():
                b = ''
                ord = Order.objects.filter(id=form.cleaned_data['order_number'])
                for a in ord:
                    b = a.book_name
                Order.objects.filter(id=form.cleaned_data['order_number']).delete()
                return orderdelconf(request, b)

        order = Order.objects.filter(mobile=request.session['mobile'])
        total_price = 0
        if order:
            for i in order:
                total_price += i.price
        return render(request, 'home/order_details.html',{'order':order,'total_price':total_price,'form':form})
    else:
        return login(request)

def orderdelconf(request, b):
    print(b)
    return render(request, 'home/orderdelconf.html',{'book':b})
