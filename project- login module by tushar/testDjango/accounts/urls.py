from django.conf.urls import patterns, url
from .views import home

urlpatterns = patterns('', url(
    r'^login/$',
    'django.contrib.auth.views.login',
    name='login',
    kwargs={'template_name': 'accounts/login.html'}
),
                       url(
                           r'^logout/$',
                           'django.contrib.auth.views.logout',
                           name='logout',
                           kwargs={'next_page': '/accounts/home/'}
                       ),
                       url(
                           r'^home/$',
                           home,
                           name='home',
                       )
                       )
