from django.db import models

class Listofcoefficient(models.Model):
    manager = models.OneToOneField('Manager', models.DO_NOTHING, db_column='manager', primary_key=True)
    minimumwagegm = models.IntegerField()
    timetocompletethetaskti = models.SmallIntegerField()
    coefficientofcosttimetc = models.SmallIntegerField()
    taskcomplexitydi = models.SmallIntegerField()
    coefficientoftaskcomplexityde = models.SmallIntegerField()
    coefficientofnatureofworkci = models.FloatField()
    forconvertedintocashtb = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'listofcoefficient'


class Manager(models.Model):
    login = models.OneToOneField('Useraccount', models.DO_NOTHING, db_column='login', primary_key=True)
    lastname = models.CharField(max_length=30)
    firstname = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'manager'


class Performer(models.Model):
    login = models.OneToOneField('Useraccount', models.DO_NOTHING, db_column='login', primary_key=True)
    lastname = models.CharField(max_length=30)
    firstname = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)
    grade = models.CharField(max_length=20)
    manager = models.ForeignKey(Manager, models.DO_NOTHING, db_column='manager')

    class Meta:
        managed = False
        db_table = 'performer'


class Task(models.Model):
    taskid = models.AutoField(primary_key=True)
    taskname = models.CharField(max_length=50)
    aboutoftask = models.CharField(max_length=100)
    periodofexecution = models.DateField()
    dateofcompletion = models.DateField(blank=True, null=True)
    taskcomplexity = models.SmallIntegerField()
    timetocompletethetask = models.SmallIntegerField()
    taskstatus = models.CharField(max_length=20)
    natureofthetask = models.CharField(max_length=50)
    taskperformer = models.ForeignKey(Performer, models.DO_NOTHING, db_column='taskperformer', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'task'


class Useraccount(models.Model):
    login = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=50)
    accountstatus = models.BooleanField()
    datetimeauthorized = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'useraccount'