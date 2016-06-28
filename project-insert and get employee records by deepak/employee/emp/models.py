from django.db import models


class employee(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    sal = models.IntegerField(default=0)

    def __str__(self):
        return (self.fname + self.lname + str(self.sal))
