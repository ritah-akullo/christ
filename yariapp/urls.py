# landing_page/urls.py

from django.urls import path
from yariapp import views
from django.contrib.auth import views as auth_views
# from .views import CustomPasswordResetView


urlpatterns = [
    path('', views.landing_page, name='index.html'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('home/', views.home_page, name='home.html'),
    path('home/baby_list/', views.baby_list, name='baby_list'),
    path('home/', views.home_page, name='home'),
    path('home/sitters_list/', views.sitters, name='sitters_list'),
    path('pro_list/', views.pro_list, name='pro_list'),
    path('procurement/', views.pro, name='procurement'),
    path('shop/', views.dollshop, name='shop.html'),
    path('shop_list/', views.shop_list, name='shop_list'),
    path('sell_doll/', views.proo, name='sell_doll'),
    path('sell_doll/<int:pk>/', views.dollsell, name='sell_doll'),
    path('selldoll_list/', views.dollsell_list, name='selldoll_list'),


    path('baby_edit/<int:id>/', views.baby_edit, name='baby_edit'),
    path('baby/', views.baby, name='baby'),
    path('baby_list/', views.baby_list, name='baby_list'),
    path('arrival/', views.arrival, name='arrival'),
    path('depature/', views.depature, name='depature'),
    path('depature_list/', views.depature_list, name='depature_list'),

    path('payment/', views.payment, name= 'payment'),
    path('payment_list/', views.payment_list, name= 'payment_list'),
    path('arrival_list/', views.arrival_list, name='arrival_list'),
    path('baby_list/sitters_list.html', views.sitters_list, name='sitters_list'),
    path('baby_list/onduty_list.html', views.onduty_list, name='onduty_list'),
    path('baby_list/baby_list.html', views.baby_list, name='baby_list'),
    path('baby_list/payment_list.html', views.payment_list, name='payment_list'),
    path('payment/', views.payment_page, name='payment'),
    path('baby/', views.baby_page, name='baby'),
#sitters
    path('sitters/', views.sitters, name='sitters'),
    path('onduty/', views.onduty, name='onduty'),
    path('onduty_list/', views.onduty_list, name='onduty_list'),
    path('sitters_list/', views.sitters_list, name='sitters_list'),
    path('sitters/baby_list.html', views.baby_list, name='baby_list'),
    path('s_payment_list/', views.sitters_payment_list, name='sitters_payment_list'),
    path('pay/', views.payform, name='pay'),
    
     #procurements
     path('shop/', views.dollshop, name='shop'),
     path('shop_list/', views.shop_list, name='shop_list'),
     path('pro_list/', views.pro_list, name='pro_list'),
     path('procurement/', views.pro, name='procurement',)


]

    
    

