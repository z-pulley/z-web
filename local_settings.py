# local settings
import logging
import os.path

DIRNAME = os.path.dirname(os.path.abspath(__file__))

ROOT_RELATIVE_URL = '/'
ROOT_URL = 'http://new.z-pulley.com' + ROOT_RELATIVE_URL
LOGIN_URL = ROOT_URL + 'accounts/login/'
MEDIA_URL = ROOT_URL + 'media/'
ADMIN_MEDIA_PREFIX = ROOT_URL + 'admin-media/'

#
# Configure app logging for debug purposes.  Disabled by default in non-debug environments
#
#
# Modules wishing to use logging should:
# import logging
# logging.getLogger(DESCRIPTOR) # DESCRIPTOR is the logger with the name DESCRIPTOR
# log.debug('message for debug')
# log.warning('message for warning')
#
if 1:
    LOGFILE="z_web.log"
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename=os.path.join(DIRNAME,LOGFILE),
                        filemode='w')
    logging.info("Infinity Tool Started")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'z_web',
        'USER': 'aaronr',
        'PASSWORD': 'aaronr',
        'HOST': '',
        'PORT': '',
    },
}       
