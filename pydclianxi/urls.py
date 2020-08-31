"""pydclianxi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import myadmin, dcapi  # .表示当前路径，表示从当前路径引入myadmin
urlpatterns = [
    path('', myadmin.hello),    #表示当没有自己填路径时，用myadmin下的hello去响应
    path('admin/', admin.site.urls),
    path('hello/', myadmin.hello),     #表示当请求http://127.0.0.1:8000/hello/路径，就调用myadmin里面的hello函数
    path('test/', myadmin.test),       #表示当请求http://127.0.0.1:8000/test/路径，就调用myadmin里面的test函数
    path('testdata/', myadmin.testdata),
    path('foodadd/', myadmin.foodadd),    #表示当请求http://127.0.0.1:8000/foodadd/路径，就调用myadmin里面的foodadd函数
    path('foodaddpost/', myadmin.foodaddpost),   #当表单页面foodadd点保存后，就去myadmin里面找对应处理的函数foodaddpost
    path('foodlist/', myadmin.foodlist),
    path('foodedit/', myadmin.foodedit),
    path('foodeditpost/', myadmin.foodeditpost),
    path('fooddelete/', myadmin.fooddelete),
    path('orderlist/', myadmin.orderlist),
    path('orderdelete/', myadmin.orderdelete),
    path('orderview/', myadmin.orderview),
    path('login/', myadmin.login),
    path('loginpost/', myadmin.loginpost),
    path('dcapi/login', dcapi.login),
    path('dcapi/getfoodlistbyrandom', dcapi.getfoodlistbyrandom),
    path('dcapi/getfoodbyid', dcapi.getfoodbyid),
    path('dcapi/getfoodlist', dcapi.getfoodlist),
    path('dcapi/addtocar', dcapi.addtocar),
    path('dcapi/getcarlist', dcapi.getcarlist),
    path('dcapi/changecarnum', dcapi.changecarnum),
    path('dcapi/deleteitembyid', dcapi.deleteitembyid),
    path('dcapi/saveorder', dcapi.saveorder),

    path('uilunbo/', myadmin.uilunbo),
    path('uilunbopost/', myadmin.uilunbopost),
    path('uilunbolist/', myadmin.uilunbolist),
    path('lunbodelete/', myadmin.lunbodelete),
    path('uichushi/', myadmin.uichushi),
    path('uichushipost/', myadmin.uichushipost),
    path('uichushilist/', myadmin.uichushilist),
    path('chushidelete/', myadmin.chushidelete),
    path('dcapi/chushilist', dcapi.chushilist),
    path('dcapi/tiandianlist', dcapi.tiandianlist),
    path('uitiandian/', myadmin.uitiandian),
    path('uitiandianpost/', myadmin.uitiandianpost),
    path('uitiandianlist/', myadmin.uitiandianlist),
    path('uitiandiandelete/', myadmin.uitiandiandelete),
    path('dcapi/getmyorderlist', dcapi.getmyorderlist),
    path('dcapi/reg', dcapi.reg),
    path('dcapi/gettiandianbyid', dcapi.gettiandianbyid),
    path('dcapi/message', dcapi.message),
    path('dcapi/messagelist', dcapi.messagelist),
    path('messagelist/', myadmin.messagelist),
    path('messagedelete/', myadmin.messagedelete),
    path('messagereply/', myadmin.messagereply),
    path('messagereplypost/', myadmin.messagereplypost),
    path('memberlist/', myadmin.memberlist),
    path('memberdelete/', myadmin.memberdelete),
    path('uitiandianedit/', myadmin.uitiandianedit),
    path('uitiandianeditpost/', myadmin.uitiandianeditpost),


]
