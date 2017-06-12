from django.conf.urls import url
from django.contrib.auth import views as auth_views
from digiTech import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login$', auth_views.login,  {'template_name': 'digiTech/login.html'}, name='login'),
    url(r'^notfound$', views.handler_404, name='404'),
]
