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

#RetrieveAPIView only return one object
#To retrieve object using primary key
class IPDetailList(RetrieveAPIView):
    queryset = IPdata.objects.all()
    serializer_class = IPDetailSerializer
