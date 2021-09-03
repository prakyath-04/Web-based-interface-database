"""dbsite URL Configuration

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
# from django.contrib import admin
# from django.urls import path
#
from django.contrib import admin
from django.urls import path,re_path
from myapp.views import hello_geek
from myapp.views import index
from myapp import views
# from django.contrib.auth.views import LoginView

# from django.views.generic.base import T
# emplateView
# from myapp.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^home.*',index,name='home'),
    path('register', views.signup_request,name='register'),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    path("cust_info",views.save_record_cust,name = "cust_info"),
    re_path(r'^ins_form.*', views.save_insurance, name='ins_form'),
    path("vform", views.save_vehicle, name="vform"),
    path("dform", views.save_driver, name="dform"),
    path("hform", views.save_home, name="hform"),
    path("cust_rec",views.get_customer_record,name='cust_rec'),
    path("ins_rec", views.get_insurance_record, name='ins_rec'),
    path("all_cust",views.get_all_customers,name='all_cust'),
    path("all_ins",views.get_all_insurance,name='all_ins'),
    path("upd_cust", views.update_cust, name='upd_cust'),
    re_path(r'^upd_cust_db.*', views.update_cust_db, name='upd_cust_db'),
    path("del_cust",views.delete_cust_record,name='del_cust'),
    path("inv",views.get_invoice,name='inv')

    # path('customers/', index),
]
