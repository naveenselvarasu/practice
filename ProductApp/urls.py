"""Product URL Configuration

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
from django import views
from django.contrib import admin
from django.urls import path
from ProductApp import views

urlpatterns = [
    path("save_product_group/",views.save_product_group),
    path("save_product/",views.save_product),
    path("read_product_group/",views.read_product_group),
    path("read_product/",views.read_product),
    path("update_product_group/",views.update_product_group),
    path("update_product/",views.update_product),
    path("delete_product_group/",views.delete_product_group),
    path("delete_product/",views.delete_product),


]
