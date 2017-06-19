from django.conf.urls import url
from django.contrib.auth import views as auth_views
from digiTech import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^registration$', views.registration, name='registration'),
    url(r'^notfound$', views.handler_404, name='404'),
    url(r'^login$', views.login, name='login'),
    url(r'^password_reset$', views.password_reset, name='password_reset'),
]
