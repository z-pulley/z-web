from django.db import models
#from django.contrib.gis.db import models

from django.db import models

class MydataArchive(models.Model):
    user_id = models.BigIntegerField()
    class Meta:
        db_table = u'test_model'

