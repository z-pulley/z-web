from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.static import serve

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       (r'', include('z_web.urls')),
                    
                        # Enable the admin:
                        (r'^admin/', include(admin.site.urls)),

                        # Static media files
                        (r'^media/(.*)$','django.views.static.serve',{'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
                        (r'^admin-media/(.*)$','django.views.static.serve',{'document_root': settings.ADMIN_MEDIA_ROOT, 'show_indexes': True}),

)
