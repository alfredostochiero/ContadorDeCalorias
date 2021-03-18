from django.urls import path
from .views import index,delete_consume

urlpatterns = [
    path('',index, name='index'),
    path('delete/<int:id>/',delete_consume,name='delete')

]
