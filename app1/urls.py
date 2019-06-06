from django.conf.urls import url
from app1 import views

app_name='app1'

urlpatterns=[
         url(r'^contacts/', views.contactPage,name='contactPage'),

         #<<< By HME >>>
         url(r'^numbers/', views.numberPage,name='NumberPage'),
         url(r'^contactList/', views.ContactListPage,name='ContactListPage'),



]
