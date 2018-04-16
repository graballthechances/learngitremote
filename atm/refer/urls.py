from django.conf.urls import url
from . import views

urlpatterns=[
url(r'^$',views.mainpage,name='mainpage'),
url(r'^deposit/$',views.deposit_input,name='deposit'),
url(r'^depositfinish/$',views.deposit_finish,name='depositfinish'),
url(r'^withdraw/$',views.withdraw_input,name='withdraw'),
url(r'^withdrawfinish/$',views.withdraw_finish,name='withdrawfinish'),
url(r'^transfer/$',views.transfer_input,name='transfer'),
url(r'^transferfinish/$',views.transfer_finish,name='transferfinish'),
url(r'^inquery/$',views.inquery,name='inquery'),
url(r'^changepassword/$',views.change_password,name='changepassword'),
url(r'^changefinish/$',views.change_finish,name='changefinish'),
url(r'^ecashmainpage/$',views.ecash_mainpage,name='ecashmainpage'),
url(r'ecashbalance/$',views.ecash_balance,name='ecashbalance'),
url(r'ecashin/$',views.ecash_in,name='ecashin'),
url(r'ecashout/$',views.ecash_out,name='ecashout'),
]