from django.db   import models

from core.models import TimeStampModel

class User(TimeStampModel):
    account  = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    class Meta:
        db_table = 'users'