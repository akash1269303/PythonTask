"""Short URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from shortenurl import views
from shortenurl.views import Redirector

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fetching/',views.Shortner.as_view()),
    path('create/',views.ShortnerCreate.as_view()),
    path('<str:shorten_url>/',views.Redirector.as_view(),name='redirector'),
    path('delete/<str:id>',views.UrlDestroy.as_view()),
    path('get_one_url/<str:id>',views.GetUrl.as_view()),
]
