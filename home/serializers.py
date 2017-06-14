from rest_framework.serializers import ModelSerializer
from .models import IPdata

class IPDetailSerializer(ModelSerializer):

    class Meta:
        model = IPdata
        #fields = '__all__'
        fields = ('ip_address','port_no','country','anonymity','HTTPS','last_modified')


class IPListSearializer(ModelSerializer):

    class Meta:
        model = IPdata
        fields = ('ip_address','port_no','country')