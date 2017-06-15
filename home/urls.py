from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.IPListAPIView.as_view(), name="ListOfAll"),
    url(r'^(?P<pk>(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]'
        r'|25[0-5]))/$', views.IPDetailList.as_view(), name="search"),
    url(r'^(?P<pk>(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]'
        r'|25[0-5])+)/edit/$', views.IPUpdateAPIView.as_view(), name="edit"),
    url(r'^(?P<pk>(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]'
        r'|25[0-5])+)/delete/$', views.IPDeleteAPIView.as_view(), name="delete"),
    url(r'^create/$', views.IPCreateAPIView.as_view(), name="create"),
    url(r'^(?P<country>.+)/$', views.IPCountryListAPIView.as_view(), name="ListOfCountry"),

]
