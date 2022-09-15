"""day004 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from app import views#引入站点app下的views文件
from django.conf.urls.static import static#导入静态资源框架
from django.conf import  settings
urlpatterns = [
    path("zhuce",views.zhuce),
    path("denglu",views.denglu),
    path("private",views.private),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
