from django.conf.urls.defaults import *
from whatismyip import views

urlpatterns = patterns('',               
    url(r'$', 'views.main',name="main"),
)
