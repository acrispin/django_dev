import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):              # __str__ on Python 3
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):              # __str__ on Python 3
        return self.choice_text

class Test(models.Model):
    # id = models.AutoField(primary_key=True) # django lo crea automaticamente sino se especifica un primary_key
    iden = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=4, unique=True)
    name = models.CharField(max_length=50, db_column='fullname')
    period = models.CharField(max_length=6, db_index=True)
    dni = models.CharField(max_length=8, blank=True)
    email = models.EmailField(max_length=75, null=True)
    comments = models.TextField(null=True)
    num = models.IntegerField(default=0, null=True)
    cost = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    vent = models.DecimalField(max_digits=13, decimal_places=4, null=True)
    total = models.FloatField(null=True)
    sec = models.SmallIntegerField(null=True)
    big = models.BigIntegerField(null=True)
    flag = models.NullBooleanField()
    active = models.BooleanField(default=True)
    cum_date = models.DateField(null=True)
    reg_date = models.DateTimeField(auto_now_add=True, null=True)
    reg_user = models.CharField(max_length=30, null=True)
    mod_date = models.DateTimeField(auto_now=True, null=True)
    mod_user = models.CharField(max_length=30, null=True)

    def __unicode__(self):              # __str__ on Python 3
        return "{0} {1}".format(self.code, self.name)
