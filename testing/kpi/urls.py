from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.kpi, name='kpi'),
    #url(r'^add', views.kpi_add, name='kpi_add'),
]