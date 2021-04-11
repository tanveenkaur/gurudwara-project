from django.urls import path
from . import views


urlpatterns=[
path('',views.index,name='index'),
path('submit/',views.submit,name='submit'),
path('search/',views.search,name='search'),
path('edit/<int:id>/',views.edit,name='edit'),
path('delete/<int:id>/',views.delete,name='delete'),
path('update',views.update,name='update')


]
