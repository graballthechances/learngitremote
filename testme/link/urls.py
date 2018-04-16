from django.conf.urls import url
from . import views
# from django.contrib import admin

urlpatterns=[
url(r'first/$',views.first),
url(r'second/$',views.second)
]