import xadmin
from django.contrib import admin

# Register your models here.
from others.models import OthersInfo

xadmin.site.register(OthersInfo)
