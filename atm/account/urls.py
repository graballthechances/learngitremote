from django.conf.urls import url,include
from . import views

urlpatterns=[
url(r'^login/$',views.alogin,name='alogin'),
url(r'^register/$',views.register,name='register'),
url(r'^logout/$',views.alogout,name='alogout'),
]