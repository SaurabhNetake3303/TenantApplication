"""RealEstate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include

from .import views

urlpatterns = [

    path('', views.index, name="index"),
    path('login', views.login, name="login"),
    
    path('registration', views.registration, name="registration"),

    path('register', views.register, name="register"),

    path('add', views.add, name="add"),

    path('register_tenant', views.register_tenant, name="register_tenant"),

    path('Tenant_Entry' , views.Tenant_Entry , name='Tenant_Entry'),
    path('M_Meter_Report' , views.M_Meter_Report , name='M_Meter_Report'),
    path('S_Meter_Report' , views.S_Meter_Report , name='S_Meter_Report'),
    path('Tanker_Report' , views.Tanker_Report , name='Tanker_Report'),
    path('showresults' , views.showresults , name='showresults'),
    path('showMeterResults' , views.showMeterResults , name='showMeterResults'),
    path('Show_Sub_MeterResults' , views.Show_Sub_MeterResults , name='Show_Sub_MeterResults'),
    path('Show_Tanker_Results' , views.Show_Tanker_Results , name='Show_Tanker_Results'),

    path('login_check', views.login_check, name="login_check"),

    path('logout', views.logout, name="logout"),

    path('Modify' , views.Modify, name="Modify"),
    path('update_data' , views.update_data,name="update_data"),

    path('meter_entry', views.meter_entry, name="meter_entry"),
    path('mainmeter', views.mainmeter, name="mainmeter"),
    path('mainmeter_edit', views.mainmeter_edit, name="mainmeter_edit"),
    path('Update_Mainmeter', views.Update_Mainmeter, name="Update_Mainmeter"),

    path('sub_meter', views.sub_meter, name="sub_meter"),
    path('submeter', views.submeter, name="submeter"),
    path('submeter_edit', views.submeter_edit, name="submeter_edit"),
    path('Update_Submeter', views.Update_Submeter, name="Update_Submeter"),

    path('tanker_entry', views.tanker_entry, name="tanker_entry"),
    path('tanker_data', views.tanker_data, name="tanker_data"),
    path('tanker_data_edit', views.tanker_data_edit, name="tanker_data_edit"),
    path('Update_Tanker', views.Update_Tanker, name="Update_Tanker"),
    
    path('delete', views.delete,name="delete"),
    path('delete_Mainmeter', views.delete_Mainmeter,name="delete_Mainmeter"),
    path('delete_Submeter', views.delete_Submeter,name="delete_Submeter"),
    path('delete_Tanker', views.delete_Tanker,name="delete_Tanker"),

]
