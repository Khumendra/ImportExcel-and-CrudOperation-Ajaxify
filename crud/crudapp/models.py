from django.db import models


class Number_store(models.Model):
    num = models.IntegerField()
    userid = models.CharField(max_length=30)

    class Meta:
        db_table = 'Number_store'


class CrudUser(models.Model):
    name = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name + " || " + self.address
