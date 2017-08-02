from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
        url(r'^student_info$', views.student_info, name='student_info')
]
