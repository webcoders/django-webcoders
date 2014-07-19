from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
    # url(r'^$', 'topship.views.home', name='home'),
    # url(r'^topship/', include('topship.foo.urls')),
    url(r"^/widgets/address/",'webcoders.views.address.get', name='address' ),

)

#urlpatterns += staticfiles_urlpatterns()