from django.urls import path,include
from .import views
urlpatterns = [
   path('register/',views.register,name="register"),
   path('login/',views.login,name="login"),
   path('create_customer/',views.create_customer,name="create_customer"),
   path('customerdetails/',views.customerDetails,name="customerDetails"),
]
