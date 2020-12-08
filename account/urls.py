from django.urls import path
from  . import  views

urlpatterns = [
    path('index', views.homepage, name='index' ),
    path('opportunity', views.opportunity_create, name='create-opportunity' ),
    path('opportunity-update/<str:pk>', views.opportunity_update, name='update-opportunity'),
    path('opportunity-delete/<str:pk>', views.opportunity_delete, name='delete-opportunity'),
    path('account', views.account_form, name='account' ),
    path('account-list', views.account_list, name='account-list' ),
    path('accountview', views.account, name='account-view' ),
    path('accountupdate/<str:pk>', views.accountUpdate, name='account-update'),
    path('account-delete/<str:pk>', views.account_delete, name='delete-account'),
    path('', views.register, name='register'),
    path('login',views.LoginPage,name='login'),
    path('logout',views.logoutPage,name='logout'),

]



