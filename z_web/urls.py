from django.conf.urls.defaults import *


urlpatterns = patterns('',
    (r'^$', 'z_web.views.home_page', {}),
    (r'^about/$', 'z_web.views.about_page', {}),
    (r'^contact/$', 'z_web.views.contact_page', {}),

)
