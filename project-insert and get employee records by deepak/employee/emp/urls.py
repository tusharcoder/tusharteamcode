from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^home/', views.home, name='home'),
    url(r'^insert/', views.insert, name='insert'),
    url(r'^doinsert/', views.doinsert, name='doinsert')
]