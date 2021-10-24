from django.db import models

from core.models import TimeStampModel
from users.models import User

class Board(TimeStampModel):
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    title   = models.CharField(max_length=50)
    body    = models.CharField(max_length=10000)

    class Meta:
        db_table = 'board'

