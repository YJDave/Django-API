from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
    )
from home.models import IPdata
from home.serializers import IPDetailSerializer, IPListSearializer

class IPDeleteAPIView(DestroyAPIView):
    queryset = IPdata.objects.all()
    serializer_class = IPDetailSerializer

class IPUpdateAPIView(UpdateAPIView):
    queryset = IPdata.objects.all()
    serializer_class = IPDetailSerializer


class IPlistAPIView(ListAPIView):
    queryset = IPdata.objects.all()
    serializer_class = IPListSearializer

    #def get_queryset(self):

class IPDetailList(RetrieveAPIView):
    queryset = IPdata.objects.all()
    serializer_class = IPDetailSerializer
    #lookup_field = 'country'



"""
#from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import IPdata
from .serializers import IPdataSerializer
from django.http import HttpResponse

from django.db.models import Q

# Create your views here.

class IPlist(APIView):


    def get_queryset(self, *args, **kwargs):
        serializer = IPlist
        queryset_list = IPdata.objects.filter(user=self.request.user)
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(country__contains=query)).distinct()
        return queryset_list

#pass all list of IP
    def get(self, request):

        all_ip = IPdata.objects.all()
        serializer = IPdataSerializer(all_ip, many=True)
        return Response(serializer.data)

    #to add new IP in list or edit it
    def post(self):
        pass

"""