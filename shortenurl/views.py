from django.shortcuts import render,redirect,HttpResponse
from .models import Link
from django.views import View
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView
from django.conf import settings
from .serializer import Linkserializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from rest_framework.response import Response
from rest_framework import viewsets


# You can check this API in POSTMAN or its also browsable API.

# fetching list of shortened URLs
class Shortner(ListAPIView):
    queryset=Link.objects.all()
    serializer_class=Linkserializers


# creating a shortened URL
class ShortnerCreate(CreateAPIView):
    serializer_class=Linkserializers


# navigate to the original URL by clicking on the shortened URL 
class Redirector(View):
    def get(self,request,shorten_url,*args,**kwargs):
        shorten_url=settings.HOST_URL+'/'+self.kwargs['shorten_url']
        redirect_link=Link.objects.filter(shorten_url=shorten_url).first().original_url
        return redirect(redirect_link)


# fetching original URL from a shortened URL
class GetUrl(APIView):
    def get(self, request,id):
        try:
            res = Link.objects.get(id=id)
            org_url=res.original_url
            return Response(org_url)
        except Link.DoesNotExist:
            message = {"error":" No is Invalid"}
            return Response(message)


# deleting shortened-URLs 
class UrlDestroy(APIView):
    def delete(self,request,id):
        res=Link.objects.filter(id=id).delete()
        if res[0] != 0:
            message = {"message": "Link is Deleted"}
        else:
            message = {"message": "Invalid ID "}
        return Response(message)











