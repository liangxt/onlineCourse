from django.conf.urls import url
from django.contrib.auth import views as auth_views
from digiTech import views

urlpatterns = [url(r'^$', views.home, name='home'),
]
