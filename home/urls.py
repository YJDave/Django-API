from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.IPlistAPIView.as_view(), name="list"),
    #url(r'^(?P<country>[\w-]+)/$', views.IPDetailList.as_view(), name="country"),
    url(r'^(?P<pk>\d+)/$', views.IPDetailList.as_view(), name="search"),
    url(r'^(?P<pk>\d+)/edit/$', views.IPUpdateAPIView.as_view(), name="edit"),
    url(r'^(?P<pk>\d+)/delete/$', views.IPDeleteAPIView.as_view(), name="delete"),

]
