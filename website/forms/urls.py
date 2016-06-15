from django.conf.urls import url, include
from . import views

app_name = 'forms'

urlpatterns = [
    # URL FOR INDEX PAGE OF THE FORM
    url(r'^$', views.index, name="index"),
    url(r'^submit_form', views.submit, name="insert")
]
