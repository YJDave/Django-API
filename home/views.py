from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView
    )
#authentication permissions
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)

from home.models import IPdata
from home.serializers import (
    IPDetailSerializer,
    IPListSerializer,
    IPCreateUpdateSerializer,
)

#home/create
class IPCreateAPIView(CreateAPIView):
    queryset = IPdata.objects.all()
    serializer_class = IPCreateUpdateSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]

#home/specific_object/delete
class IPDeleteAPIView(DestroyAPIView):
    queryset = IPdata.objects.all()
    serializer_class = IPDetailSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class IPUpdateAPIView(RetrieveUpdateAPIView):
    queryset = IPdata.objects.all()
    serializer_class = IPCreateUpdateSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]


#home/?country=country_name
class IPListAPIView(ListAPIView):

    serializer_class = IPListSerializer
    # permission_class = [AllowAny]
    def get_queryset(self):

        queryset = IPdata.objects.all()
        query = self.request.query_params.get('country', None)
        if query is not None:
            queryset = queryset.filter(country__iexact=query)      #for case insensitive search
        return queryset

#home/country_name
class IPCountryListAPIView(ListAPIView):
    serializer_class = IPListSerializer
    #permission_class = [AllowAny]
    def get_queryset(self):
        country_name = self.kwargs['country']
        return IPdata.objects.filter(country__iexact=country_name)
    #To search even for substring search:
    #   return IPdata.objects.filter(country__icontains=country_name)

#RetrieveAPIView only return one object
#To retrieve object using primary key (Here IP address is primary key)
#home/specific_object's_ip_address
class IPDetailList(RetrieveAPIView):
    queryset = IPdata.objects.all()
    serializer_class = IPDetailSerializer
    # permission_class = [AllowAny]