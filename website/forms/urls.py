from django.conf.urls import url, include
from . import views

app_name = 'forms'

urlpatterns = [
    # URL FOR INDEX PAGE OF THE FORM
    url(r'^$', views.index, name="index"),
	# CALLING FUNCTION TO INSERT VALUES INTO DATABASE
    url(r'^submit_f1', views.submit_f1, name="submit_f1"),
]
