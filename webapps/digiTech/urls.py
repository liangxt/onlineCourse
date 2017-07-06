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
    url(r'^chechout$', views.checkout, name='checkout'),
    url(r'^all_courses$', views.all_course, name='all_courses'),
    url(r'^team$', views.team, name='team'),
    url(r'^course$', views.course, name='course'),
    url(r'^course_module$', views.course_module, name='course_module'),
    url(r'^single_module$', views.single_module, name='single_module'),
    url(r'^profile_edit$', views.profile_edit, name='profile_edit'),
]
