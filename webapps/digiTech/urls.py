from django.conf.urls import url
from digiTech import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^registration$', views.registration, name='registration'),
    url(r'^notfound$', views.handler_404, name='404'),
    url(r'^login$', views.user_authenticate, name='login'),
    url(r'^password_reset/(?P<username>.+)/(?P<token>.+)$', views.password_reset, name='password_reset'),
    url(r'^password_forget', views.password_forget, name='password_forget'),
    url(r'^account_activate/(?P<username>.+)/(?P<token>.+)$', views.account_activate, name='account_activate'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^checkout$', views.checkout, name='checkout'),
]
