from django.db import models



# Create your models here.
class IPdata(models.Model):

    #id = models.AutoField(primary_key=True)
    ip_address = models.GenericIPAddressField(protocol='both', unpack_ipv4=False, primary_key=True)
    country = models.CharField(max_length=100)
    #values for PositiveSmallIntegerField is 0 to 32767
    #port limit is 65536 so
    port_no = models.PositiveIntegerField()
    anonymity = models.CharField(max_length=50, default="Low")
    last_modified = models.DateTimeField(auto_now=True)
    HTTPS = models.CharField(max_length=3, default="No")

    def __str__(self):
        return self.ip_address + ' - ' +  self.country + ' - ' +  str(self.port_no) + ' - ' +  self.anonymity + ' - '\
        +  str(self.last_modified) + ' - ' +  self.HTTPS