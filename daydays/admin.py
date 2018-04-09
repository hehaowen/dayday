from django.contrib import admin
from .models import *
# Register your models here.
import xadmin

xadmin.site.register(UserInfo)
