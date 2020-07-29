from django.urls import path
from myapp import views
app_name="myapp" #is used to create the namespace\ 

urlpatterns = [
    path('',views.home,name="home"),
    path('base',views.base,name="base"),
    path('child/',views.child,name="child"),
]
