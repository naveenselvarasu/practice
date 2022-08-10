from http.client import ImproperConnectionState
import imp
from urllib import response
from django.shortcuts import render
from requests import delete
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import *


# Create your views here.

# "create view"

@api_view(["POST"])
def save_product_group(request):
    data =request.data
    print(data)
    if ProductGroup.objects.filter(type = data["type"]).exists():
        result = "this product group is already existed"
    else:
        ProductGroup.objects.create(type=data["type"])
        result = f"{data} is successfuly created"

    return Response(data = result)

from asgiref.sync import sync_to_async

@api_view(["POST"])
def save_product(request):
    print(request.data)
    data =request.data
    print(data)
    if Product.objects.filter(variety=data["variety"]).exists():
        result = "this variety is already existed"
    else:
        Product.objects.create(
                        productgroup_id=data["productgroup_id"],
                        variety=data["variety"],
                        quantity = data["quantity"],
                        price = data["price"],
                        expiry_date = data["expiry_date"],
                        paking_date = data["paking_date"]

                        )
        
        result = f"{data} is successfuly created"

    return Response(data = result)


# read view

@api_view(["GET"])
def read_product_group(request):
    product_group_objs = ProductGroup.objects.all().values()

    return Response(data = product_group_objs)


@api_view(["GET"])
def read_product(request):
    product_objs = Product.objects.all().values()

    return Response(data = product_objs)


# update view

@api_view(["PUT"])
def update_product_group(request):
    data = request.data
    if ProductGroup.objects.filter(type = data["type"]).exists():
        ProductGroup.objects.filter(type = data["type"]).update(type = data["type"])
        return Response(data ="you are successfully updated obj")
    else:
        return Response(data ="you are data is not already exist")   
        

@api_view(["PUT"])
def update_product(request):
    data = request.data
    if Product.objects.filter(variety = data["variety"]).exists():
        Product.objects.filter(
            variety = data["variety"]).update(
                                            productgroup_id=data["productgroup_id"],

                                            variety=data["variety"],
                                            quantity = data["quantity"],
                                            price = data["price"],
                                            expiry_date = data["expiry_date"],
                                            paking_date = data["paking_date"]
                                            )

        return Response(data ="you are successfully updated obj")
    else:
        return Response(data ="you are data is not already exist")   



# delete view 

@api_view(["POST"])
def delete_product_group(request):
    data = request.data
    if ProductGroup.objects.all().filter(type = data["type"]).exists():
        ProductGroup.objects.all().filter(type = data["type"]).delete()
        Product.objects.all().filter(productgroup = data["type"]).delete()
        return Response(data ="you are successfully deleted obj")
    else:
        return Response(data ="you are data is not already exist")   
        

@api_view(["POST"])
def delete_product(request):
    data = request.data
    if Product.objects.all().filter(variety = data["variety"]).exists():
        Product.objects.all().filter(variety = data["variety"]).delete()
        return Response(data ="you are successfully deleted obj")
    else:
        return Response(data ="you are data is not already exist")  
        
        
        

# delete view 

@api_view(["POST"])
def delete_product_group(request):
    data = request.data
    if ProductGroup.objects.all().filter(type = data["type"]).exists():
        ProductGroup.objects.all().filter(type = data["type"]).delete()
        Product.objects.all().filter(productgroup = data["type"]).delete()
        return Response(data ="you are successfully deleted obj")
    else:
        return Response(data ="you are data is not already exist")
        
        
        

        
        
        



  
