from django.db import models

class Useraccount(models.Model):
    login = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=50)
    accountstatus = models.BooleanField()
    datetimeauthorized = models.DateTimeField()

    class Meta:
        db_table = 'useraccount'