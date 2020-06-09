"""Movie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include,path
from Thriller import views as tviews

urlpatterns = [
    path('',include('Thriller.urls')),
    path('01.html',tviews.one),
    path('02.html',tviews.two),
    path('03.html',tviews.three),
    path('04.html',tviews.four),
    path('05.html',tviews.five),
    path('06.html',tviews.six),
    path('07.html',tviews.seven),
    path('08.html',tviews.eight),
    path('09.html',tviews.nine),
    path('10.html',tviews.ten),
    path('admin/', admin.site.urls),
]
