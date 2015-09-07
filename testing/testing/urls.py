from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
    # Examples:
    # url(r'^$', 'testing.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('kpi.urls'), name='kpi'),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', auth_views.login),
    url(r'^accounts/logout/$', auth_views.logout_then_login),
    url(r'^nested_admin/', include('nested_admin.urls')),
]
