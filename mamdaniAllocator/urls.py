from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^ramfunction$', views.ramfunction),
    url(r'^cpufunction$', views.cpufunction),
    url(r'^diskfunction$', views.diskfunction),
    url(r'^outputfunction$', views.Outputfunction),
    url(r'^result$', views.result),
    url(r'^cpuset$', views.Cpuset),
    url(r'^ramset$', views.Ramset),
url(r'^outputset$', views.Outputset),
url(r'^diskset$', views.Diskset),
    url(r'^monitor/',
        views.monitor,
        name='monitor'),
]