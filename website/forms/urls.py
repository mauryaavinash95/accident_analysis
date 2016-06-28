from django.conf.urls import url, include
from . import views

app_name = 'forms'

urlpatterns = [
    # URL FOR INDEX PAGE OF THE FORM
    url(r'^$', views.index, name="index"),
	url(r'^form2/', views.form2, name="form2"),
    url(r'^submit_form1', views.submit1, name="submit1"),
    url(r'^submit_form2', views.submit2, name="submit2"),
    #url(r'^submit_form3', views.submit3, name="submit3"),
    #url(r'^submit_form4', views.submit4, name="submit4"),

]
