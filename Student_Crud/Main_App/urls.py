from django.urls import path, include
from .views import *

urlpatterns = [
    path('login/', include('django.contrib.auth.urls'), name='login'),
    path('', Login, name='login'),
    path('list/', List, name='list'),
    path('insert_form/', Student_Entry_Form, name='insert_form'),
    path('insert/', Insert_db, name='insert_db'),
    path('edit/<int:id>', Edit, name='edit'),
    path('delete/<int:id>', Delete, name='delete')
]