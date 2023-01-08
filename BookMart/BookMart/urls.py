"""BookMart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from home import views as v1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', v1.home, name='home'),
    path('register/', v1.register, name='register'),
    path('login/', v1.logincheck, name='logincheck'),
    path('loginconf/', v1.loginconf, name='loginconf'),
    path('logout/', v1.logout, name='logout'),
    path('profile/', v1.profile, name='profile'),
    path('profile_update/', v1.profile_update, name='profile_update'),
    path('update_confirm/', v1.update_confirm, name='update_confirm'),
    path('order/<book>/<author>/<price>/', v1.order, name='order'),
    path('order_details/', v1.order_details, name='order_details'),
    path('langoption/', v1.langoption, name='langoption'),
    path('authors/', v1.authors, name='authors'),
    path('kannada_books/', include('kannada_books.urls')),
    path('english_books/', include('english_books.urls')),
]
