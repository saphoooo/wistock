from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'wistock.views.home', name='home'),
    url(r'^home$', 'wistock.views.home', name='home'),
    url(r'^login$', 'wistock.views.login', name='login'),
    url(r'^main$', 'wistock.views.main', name='main'),
    url(r'^myadmin$', 'wistock.views.myadmin', name='myadmin'),
    #url(r'^logout$', 'wistock.views.logout', name='logout'),
    #url(r'^stocks$', 'wistock.views.stocks', name='stocks'),
    #url(r'^profile$', 'wistock.views.profile', name='profile'),
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
