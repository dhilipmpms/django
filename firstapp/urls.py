from django.urls import path 

from . import views

urlpatterns=[
      path('',views.index,name='index'),
      path('register',views.register)
     # path('submit',views.submit)
     
    
]