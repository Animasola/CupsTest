from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'my_info.views.info_page', name='home'),
    # url(r'^cups_profile/', include('cups_profile.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
