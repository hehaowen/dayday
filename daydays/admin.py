from django.contrib import admin
from .models import *
# Register your models here.
import xadmin
from xadmin import views


class BaseSetting(object):
    enable_themes = False
    use_bootswatch = True


class GlobalSettings(object):
    # 整体配置
    site_title = '京东生鲜后台管理系统'
    site_footer = '贺浩文'
    menu_style = 'accordion'  # 菜单折叠


xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(UserInfo)
