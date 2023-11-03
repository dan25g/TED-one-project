"""
URL configuration for promarkt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from base import views
from base.views import exportRp1,exportRp2,exportRp3,exportRp4,exportRp5,exportRp6,exportRp7,exportRp8

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name='home'),
    path('report/', include(('report.urls', 'report'))),
    path('export_reporte_1/', exportRp1, name='export_reporte1'),
    path('export_reporte_2/', exportRp2, name='export_reporte2'),
    path('export_reporte_3/', exportRp3, name='export_reporte3'),
    path('export_reporte_4/', exportRp4, name='export_reporte4'),
    path('export_reporte_5/', exportRp5, name='export_reporte5'),
    path('export_reporte_6/', exportRp6, name='export_reporte6'),
    path('export_reporte_7/', exportRp7, name='export_reporte7'),
    path('export_reporte_8/', exportRp8, name='export_reporte8')
]
