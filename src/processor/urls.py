from django.conf.urls import url, include
from .views import homepage, signup, login

urlpatterns = [
    url(r'^$', homepage, name='homepage' ),
    url(r'^signup/$', signup, name='signup' ),
    url(r'^login/$', login, name='login' ),
]
